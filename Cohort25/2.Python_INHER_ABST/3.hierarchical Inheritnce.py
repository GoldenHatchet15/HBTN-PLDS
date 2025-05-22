# Hierarchical Inheritance

class Appliance:
    def plug_in(self):
        return "Appliance is plugged in."

class WashingMachine(Appliance):
    def wash_clothes(self):
        return "Washing clothes..."

class Refrigerator(Appliance):
    def cool_food(self):
        return "Cooling food..."

wm = WashingMachine()
fridge = Refrigerator()
print(wm.plug_in())  # Output: Appliance is plugged in.
print(wm.wash_clothes())  # Output: Washing clothes...
print(fridge.cool_food())  # Output: Cooling food...
