import socket  # Import socket module for network communication
import json    # Import json module for serialization and deserialization

def start_server():
    """ Function to start the server and receive JSON data from the client """
    
    # Create a TCP socket (IPv4, Stream-based connection)
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    # Bind the socket to localhost and port 12345
    server_socket.bind(("localhost", 12345))
    
    # Listen for incoming connections (allow 1 connection at a time)
    server_socket.listen(1)
    print("Server listening on port 12345...")
    
    # Accept an incoming connection
    conn, addr = server_socket.accept()
    
    # Receive data from client (maximum 1024 bytes)
    data = conn.recv(1024)
    
    # Decode bytes to a string and convert JSON string into a Python dictionary
    received_dict = json.loads(data.decode("utf-8"))
    print("Received Dictionary from Client:", received_dict)
    
    # Close the connection
    conn.close()

def send_data(data):
    """ Function to send JSON data from the client to the server """
    
    # Create a TCP socket (IPv4, Stream-based connection)
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    # Connect to the server running on localhost at port 12345
    client_socket.connect(("localhost", 12345))
    
    # Convert the dictionary to a JSON string and encode it to bytes
    serialized_data = json.dumps(data).encode("utf-8")
    
    # Send the serialized JSON data to the server
    client_socket.sendall(serialized_data)
    
    # Close the client socket after sending data
    client_socket.close()

# Usage: Running server and client together
if __name__ == "__main__":
    import threading  # Import threading module to run server in parallel
    import time  # Import time module to delay execution
    
    # Start the server in a separate thread so it runs in the background
    server_thread = threading.Thread(target=start_server)
    server_thread.start()
    
    # Give the server some time to start before sending data
    time.sleep(1)  # Prevents client from connecting before server is ready
    
    # Sample dictionary data to send from the client
    sample_dict = {"name": "Alice", "age": 30, "city": "Paris"}
    
    # Send JSON data from the client to the server
    send_data(sample_dict)
    
    # Wait for the server thread to complete before ending the script
    server_thread.join()
