#!/usr/bin/env python3


# Step 1: Define a House class (Blueprint)
class House:
    def __init__(self, color, rooms):
        self.color = color  # Attribute: The color of the house
        self.rooms = rooms  # Attribute: The number of rooms

    def open_door(self):  # Method: Action the house can do
        print(f"The {self.color} house with {self.rooms} rooms has opened its door.")

# Step 2: Create a real house object from the blueprint
my_house = House("Blue", 3)

# Step 3: Access attributes (house features)
print(my_house.color)  # Output: Blue
print(my_house.rooms)  # Output: 3

# Step 4: Call a method (make the house do something)
my_house.open_door()  # Output: The Blue house with 3 rooms has opened its door.



#Breaking it Down:___________________________________________________________
#Class (House) → Acts as the blueprint for all houses.
#Object (my_house) → A real house built from the blueprint.
#Attributes (color, rooms) → Store information about the house.
#Method (open_door()) → Defines actions the house can perform.
#Just like we can build multiple houses from the same blueprint, 
#we can create multiple objects from a class with different attributes.