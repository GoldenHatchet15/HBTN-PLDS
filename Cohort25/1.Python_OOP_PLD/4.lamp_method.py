#!/usr/bin/env python3

# This is an example of a class with methods that define actions.

class Lamp:
    def __init__(self, color):  # Constructor to set lamp color
        self.color = color  

    def turn_on(self):  # Method: Defines an action
        print(f"The {self.color} lamp is now on.")

    def turn_off(self):  # Another method
        print(f"The {self.color} lamp is now off.")

# Creating objects
lamp1 = Lamp("Red")
lamp2 = Lamp("Blue")

# Calling methods
lamp1.turn_on()  # Output: The Red lamp is now on.
lamp2.turn_off()  # Output: The Blue lamp is now off.
