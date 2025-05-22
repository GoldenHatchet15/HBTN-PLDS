class Temperature:
    def __init__(self):
        self._celsius = 0  # Private attribute (using a single underscore)

    @property
    def celsius(self):  # Getter (allows reading _celsius safely)
        return self._celsius

    @celsius.setter
    def celsius(self, value):  # Setter (allows setting _celsius with validation)
        if value < -273.15:  # Temperature cannot be lower than absolute zero!
            raise ValueError("Too cold!")
        self._celsius = value

# Creating an object
temp = Temperature()

# Accessing the attribute using the getter
print(temp.celsius)  # Output: 0

# Updating the attribute using the setter
temp.celsius = 25
print(temp.celsius)  # Output: 25

# Trying to set an invalid temperature
try:
    temp.celsius = -300  # This will raise an error
except ValueError as e:
    print(e)  # Output: Too cold!
