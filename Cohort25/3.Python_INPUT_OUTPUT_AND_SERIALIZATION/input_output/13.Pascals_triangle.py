def pascal_triangle(n):
    if n <= 0:
        return []
    
    triangle = [[1]]# Initialize the triangle with the first row
    for _ in range(n - 1):
        prev_row = triangle[-1]# Get the last row
        new_row = [1] + [prev_row[i] + prev_row[i + 1] for i in range(len(prev_row) - 1)] + [1] # Calculate the next row
        triangle.append(new_row)
    
    # Print each row in a new line
    for row in triangle:
        print(row)

# Usage
pascal_triangle(5)
