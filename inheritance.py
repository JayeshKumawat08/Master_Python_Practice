import pandas as pd

class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def display_name(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")

class Student(Person):
    def __init__(self,name,age,student_id,marks):
        super().__init__(name,age)

        self.student_id = student_id
        self.marks = marks

    def display_student(self):
        super().display_name()

        print(f"Student ID: {self.student_id}")
        print(f"Marks: {self.marks}")

if __name__ == "__main__":
    print("University Student Record")

    student1 = Student("Jayesh",23,"VIT26",92.5)
    student1.display_student()