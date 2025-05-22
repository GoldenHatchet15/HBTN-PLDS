# Append to a file



def append_to_file(filename, text):
    with open(filename, "a") as file:
        file.write(text)

# Usage
append_to_file("3.example.txt", "\nAdding a new line.")


with open("3.example.txt", "r") as file:
    content = file.read()
    print(content)

 with open(filename, "a") as file:
        file.write(text_to_add + content) 