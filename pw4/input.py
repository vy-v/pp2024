from domains.student import *
from domains.course import *
import math
import numpy as np

def input_number_of_students(self):
        number_of_students = -1  
        while number_of_students < 0:
            user_input = input("Enter the number of students in the class: ")
            if user_input.isdigit():
                number_of_students = int(user_input)
            else:
                print("Please enter a valid number.")
        return number_of_students

def input_student_information(self):
        student_id = input("Enter student ID: ")
        student_name = input("Enter student name: ")
        student_dob = input("Enter student date of birth: ")
        return Student(student_id, student_name, student_dob)

def input_number_of_courses(self):
        number_of_courses = -1  
        while number_of_courses < 0:
            user_input = input("Enter the number of courses: ")
            if user_input.isdigit():
                number_of_courses = int(user_input)
            else:
                print("Please enter a valid number.")
        return number_of_courses 

def input_course_information(self):
        course_id = input("Enter course ID: ")
        course_name = input("Enter course name: ")
        course_credits = input("Enter course credits: ")
        return Course(course_id, course_name, int(course_credits))

def input_student_marks(self, course):
        marks_dict = {}
        for student in self.students:
            student_id = student.id
            while True:
                user_input = input(f"Enter mark for {student.name} (between 0 and 20): ")
                if user_input.replace('.', '').isnumeric():
                    mark = float(user_input)
                    mark = math.floor(mark * 10) / 10  
                    if 0 <= mark <= 20:
                        marks_dict[student_id] = mark
                        break
                    else:
                        print("Please enter a valid mark between 0 and 20.")
                else:
                    print("Please enter a valid value for the mark.")
        return marks_dict