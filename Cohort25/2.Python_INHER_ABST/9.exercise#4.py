from abc import ABC, abstractmethod
#parent class
class Person(ABC):
    @property
    @abstractmethod
    def role(self):
        pass

class Teacher(Person):
    @property
    def role(self):
        return "Teacher"

class Student(Person):
    @property
    def role(self):
        return "Student"

# Creating objects
teacher = Teacher()
student = Student()
print(teacher.role)  # Output: Teacher
print(student.role)  # Output: Student
