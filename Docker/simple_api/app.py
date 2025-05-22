from flask import Flask
app = Flask(__name__)

@app.route("/api/hello")
def hello():
    return {"message": "Hello, World!"}

app.run(host="0.0.0.0", port=5252)

#run flask app with:
#docker build -t flask-api .
#docker run -p 5252:5252 flask-api
#watch: http://127.0.0.1:5252/api/hello