#This script writes a string to a file.



def write_file(filename, text):
    with open(filename, "w") as file:
        file.write(text)

# Usage
write_file("2.example.txt", "Hello, Python!")