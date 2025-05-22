from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager, create_access_token, jwt_required, get_jwt_identity
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address
from flask_cors import CORS  # Import CORS
from flask import json 

app = Flask(__name__)

# ✅ Configure Database & JWT
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///tasks.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["JWT_SECRET_KEY"] = "supersecretkey"
db = SQLAlchemy(app)
jwt = JWTManager(app)

# ✅ Configure Rate Limiting
limiter = Limiter(get_remote_address, app=app, default_limits=["100 per hour"])

# ✅ Enable CORS for all routes
CORS(app, resources={r"/*": {"origins": "*"}}, supports_credentials=True)

# ✅ User Model
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True, nullable=False)
    password = db.Column(db.String(100), nullable=False)

# ✅ Task Model
class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    completed = db.Column(db.Boolean, default=False)

    def to_dict(self):
        return {"id": self.id, "title": self.title, "completed": self.completed}

# ✅ Create Database Tables
with app.app_context():
    db.create_all()

# ✅ 1. Allow CORS only for frontend requests (More Secure)
CORS(app, resources={r"/tasks/*": {"origins": ["http://localhost:3000", "http://127.0.0.1:5500"]}})

# ✅ 2. User Registration
@app.route("/register", methods=["POST"])
@limiter.limit("5 per minute")
def register():
    data = request.json
    if User.query.filter_by(username=data["username"]).first():
        return jsonify({"error": "Username already exists"}), 400

    new_user = User(username=data["username"], password=data["password"])
    db.session.add(new_user)
    db.session.commit()
    return jsonify({"message": "User registered successfully"}), 201

# ✅ 3. User Login (Returns JWT Token)
@app.route("/login", methods=["POST"])
@limiter.limit("10 per minute")
def login():
    data = request.json
    user = User.query.filter_by(username=data["username"], password=data["password"]).first()
    if user:
        token = create_access_token(identity=user.username)
        return jsonify({"token": token})
    return jsonify({"error": "Invalid credentials"}), 401

# ✅ 4. Get All Tasks (Public)
@app.route("/tasks", methods=["GET"])
def get_tasks():
    tasks = Task.query.all()
    return app.response_class(
        response=json.dumps([task.to_dict() for task in tasks], indent=4),  # ✅ Pretty-print JSON
        status=200,
        mimetype="application/json"
    )

# ✅ 5. Create a Task (Requires Authentication)
@app.route("/tasks", methods=["POST"])
@jwt_required()
@limiter.limit("10 per minute")
def create_task():
    data = request.json
    new_task = Task(title=data["title"])
    db.session.add(new_task)
    db.session.commit()
    return jsonify(new_task.to_dict()), 201

# ✅ 6. Update a Task (Requires Authentication)
@app.route("/tasks/<int:task_id>", methods=["PUT"])
@jwt_required()
@limiter.limit("10 per minute")
def update_task(task_id):
    task = Task.query.get(task_id)
    if task:
        data = request.json
        task.title = data.get("title", task.title)
        task.completed = data.get("completed", task.completed)
        db.session.commit()
        return jsonify(task.to_dict())
    return jsonify({"error": "Task not found"}), 404

# ✅ 7. Delete a Task (Requires Authentication)
@app.route("/tasks/<int:task_id>", methods=["DELETE"])
@jwt_required()
@limiter.limit("5 per minute")
def delete_task(task_id):
    task = Task.query.get(task_id)
    if task:
        db.session.delete(task)
        db.session.commit()
        return jsonify({"message": "Task deleted"}), 200
    return jsonify({"error": "Task not found"}), 404

# ✅ Run the API
if __name__ == "__main__":
    app.run(debug=True)
