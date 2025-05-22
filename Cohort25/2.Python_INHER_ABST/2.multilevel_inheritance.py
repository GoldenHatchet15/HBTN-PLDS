# Multilevel Inheritance

class Grandparent:
    def wisdom(self):
        return "Share wisdom with family."

class Parent(Grandparent):
    def guidance(self):
        return "Guide the next generation."

class Child(Parent):
    def play(self):
        return "Playing with toys."

kid = Child()
print(kid.wisdom())  # Output: Share wisdom with family.
print(kid.guidance())  # Output: Guide the next generation.
print(kid.play())  # Output: Playing with toys.
