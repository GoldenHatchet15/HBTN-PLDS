#This script reads a file and prints its content to the console.



def read_file(filename):
    with open(filename, "r") as file:
        print(file.read())

# Usage
read_file("1.example.txt")