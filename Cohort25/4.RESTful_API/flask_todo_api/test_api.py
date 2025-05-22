import requests

BASE_URL = "http://127.0.0.1:5000"

# Test user credentials
TEST_USER = {"username": "testuser", "password": "password123"}
TASK_ID = None  # This will store the task ID created

def test_register():
    """Test user registration"""
    response = requests.post(f"{BASE_URL}/register", json=TEST_USER)
    if response.status_code == 400:
        print("[INFO] User already exists, skipping registration.")
    elif response.status_code == 201:
        print("[PASS] User registered successfully.")
    else:
        print("[FAIL] Registration failed:", response.json())

def test_login():
    """Test user login and retrieve a JWT token"""
    response = requests.post(f"{BASE_URL}/login", json=TEST_USER)
    if response.status_code == 200:
        token = response.json().get("token")
        print("[PASS] Login successful. Token received.")
        return token
    else:
        print("[FAIL] Login failed:", response.json())
        return None

def test_get_tasks():
    """Test fetching all tasks"""
    response = requests.get(f"{BASE_URL}/tasks")
    if response.status_code == 200:
        print("[PASS] Retrieved tasks successfully.")
        print("Tasks:", response.json())
    else:
        print("[FAIL] Could not retrieve tasks:", response.json())

def test_create_task(token):
    """Test creating a new task"""
    global TASK_ID
    headers = {"Authorization": f"Bearer {token}"}
    data = {"title": "Learn Flask"}
    response = requests.post(f"{BASE_URL}/tasks", json=data, headers=headers)
    if response.status_code == 201:
        TASK_ID = response.json().get("id")
        print(f"[PASS] Task created successfully. ID: {TASK_ID}")
    else:
        print("[FAIL] Task creation failed:", response.json())

def test_update_task(token):
    """Test updating an existing task"""
    if TASK_ID is None:
        print("[SKIP] No task available to update.")
        return

    headers = {"Authorization": f"Bearer {token}"}
    data = {"title": "Learn Flask & Swagger", "completed": True}
    response = requests.put(f"{BASE_URL}/tasks/{TASK_ID}", json=data, headers=headers)
    
    if response.status_code == 200:
        print("[PASS] Task updated successfully.")
    else:
        print("[FAIL] Task update failed:", response.json())

def test_delete_task(token):
    """Test deleting a task"""
    if TASK_ID is None:
        print("[SKIP] No task available to delete.")
        return

    headers = {"Authorization": f"Bearer {token}"}
    response = requests.delete(f"{BASE_URL}/tasks/{TASK_ID}", headers=headers)
    
    if response.status_code == 200:
        print("[PASS] Task deleted successfully.")
    else:
        print("[FAIL] Task deletion failed:", response.json())

def run_tests():
    """Run all tests in sequence"""
    test_register()
    token = test_login()
    if token:
        test_get_tasks()
        test_create_task(token)
        test_get_tasks()  # Check if new task appears
        test_update_task(token)
        test_get_tasks()  # Check if task update reflects
        test_delete_task(token)
        test_get_tasks()  # Final check if task is gone

if __name__ == "__main__":
    run_tests()
