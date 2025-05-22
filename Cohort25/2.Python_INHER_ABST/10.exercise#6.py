from abc import ABC, abstractmethod

#parent class
class Appliance(ABC):
    @abstractmethod
    def turn_on(self):
        pass

# Trying to instantiate an abstract class
try:
    appliance = Appliance()
except TypeError as e:
    print(e)  # Output: Can't instantiate abstract class Appliance
