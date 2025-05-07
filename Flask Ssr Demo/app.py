from flask import Flask, render_template, request, redirect, url_for, jsonify
import json
import os

app = Flask(__name__)

# Load data from JSON file
DATA_FILE = 'data.json'

@app.route('/')
def home():
    return render_template('index.html') 

def load_data():
    """Load users from the JSON file and assign unique IDs if missing."""
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, 'r') as f:
            users = json.load(f)
            
            # Ensure each user has a unique ID
            for index, user in enumerate(users):
                user["id"] = index + 1  # Assign ID dynamically
            
            return users
    return []

def save_users(users):
    """Save updated users list to the JSON file."""
    with open(DATA_FILE, "w") as f:
        json.dump(users, f, indent=4)



@app.route('/users')
def users():
    data = load_data()
    return render_template('users.html', users=data)

@app.route('/user/<username>')
def user_profile(username):
    users = load_data()
    user = next((u for u in users if u.get('username') == username), None)
    
    if user:
        return render_template('profile.html', user=user)
    
    return "<h1>User not found</h1>", 404

@app.route('/submit', methods=['POST'])
def submit():
    username = request.form.get('username', 'Guest')
    return render_template('greeting.html', username=username)

@app.route('/register', methods=['POST'])
def register():
    name = request.form['name'].strip()  # Remove leading/trailing spaces
    email = request.form['email'].strip()

    # Load existing users
    users = load_data()

    # Assign a unique ID (since JSON data lacks IDs)
    new_id = max([user.get("id", 0) for user in users] + [0]) + 1

    # Auto-generate username (lowercase, no spaces)
    username = name.lower().replace(" ", "")

    # Append new user with an ID and auto-generated username
    users.append({'id': new_id, 'name': name, 'username': username, 'email': email})

    # Save updated user list
    save_users(users)

    # Redirect back to users list
    return redirect(url_for('users'))



@app.route('/delete/<int:user_id>', methods=['POST'])
def delete_user(user_id):
    """Delete a user based on ID."""
    users = load_data()
    
    # Filter out the user with the given ID
    users = [user for user in users if user["id"] != user_id]

    # Save updated list
    save_users(users)

    return redirect(url_for('users'))

if __name__ == '__main__':
    app.run(debug=True)
