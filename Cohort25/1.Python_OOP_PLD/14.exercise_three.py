class Car:
    def __init__(self, color, brand):
        self.color = color  # Attribute: Car's color
        self.brand = brand  # Attribute: Car's brand

# Creating an object (instance) of the Car class
my_car = Car("Red", "Toyota")

# Printing attributes
print(f"My car is a {my_car.color} {my_car.brand}.")  
# Output: My car is a Red Toyota.
