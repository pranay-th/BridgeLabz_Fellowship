"""
Exercise 1:
Create a class `Student` with:
- Attributes: name, roll_number, marks
- Method: `display_info()` → prints all details  
- Method: `is_passed()` → returns True if marks ≥ 40
"""

# Write your code here
class Student:
    def __init__(self,name,marks,roll_no):
        self.name = name
        self.roll_no = roll_no
        self.marks = marks

    def  display_info(self):
        print(f"Student Name:{self.name} /n Roll number:{self.roll_no} /n Marks:{self.marks}")

    def is_passed(self):
        if self.marks>=40:
            return True
        else: 
            return False

