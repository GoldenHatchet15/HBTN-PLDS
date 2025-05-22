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



# isinatance() method is used to check 
# if an object is an instance of a class 
# or a subclass of a class.

print(isinstance(mgr, Employee))  # Output: True


# issubclass() method is used to check 
# if a class is a subclass of another class.

print(issubclass(Manager, Employee))  # Output: True