# Override the method of the parent class in the child class


class Employee:
    def work(self):
        return "Completing assigned tasks."

class Manager(Employee):
    def work(self):  # Overriding the parent method
        return "Overseeing team operations."

emp = Employee()
mgr = Manager()
print(emp.work())  # Output: Completing assigned tasks.
print(mgr.work())  # Output: Overseeing team operations.
