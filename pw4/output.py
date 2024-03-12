from domains import *
import math
import numpy as np

def show_course_marks(self, course_id):
        if course_id in self.marks:
            print(f"Marks for students in course {course_id}:")
            for student_id, mark in self.marks[course_id].items():
                print(f"Student ID: {student_id}, Mark: {mark}")
        else:
            print("Invalid course ID. Please select a valid course.")
            
def list_courses(self):
        if not self.courses:
            print("No courses available.")
        else:
            print("List of courses:")
            for course in self.courses:
                print(f"{course.id}: {course.name}")

def list_students(self):
        if not self.students:
            print("No students available.")
        else:
            print("List of students:")
            for student in self.students:
                print(f"{student.id}: {student.name}")   

def calculate_gpa(self, student_id):
        total_credits = 0
        sum = 0
        for course_id in self.marks:
            if student_id in self.marks[course_id]:
                for course in self.courses:
                    if course.id == course_id:
                        course_credits = course.credits
                        sum += self.marks[course_id][student_id] * course_credits
                        total_credits += course_credits
                        break
                else:
                    course_credits = 0
        if total_credits == 0:
            return 0
        return sum / total_credits

def show_student_gpa(self, student_id):
        gpa = self.calculate_gpa(student_id)
        print(f"Student ID: {student_id}, GPA: {gpa}")

def sort_students_by_gpa(self):
        sorted_students = sorted(self.students, key=lambda student: self.calculate_gpa(student.id), reverse=True)
        return sorted_students

def show_sorted_students(self):
        sorted_students = self.sort_students_by_gpa()
        print("Students sorted by GPA descending:")
        for student in sorted_students:
            print(f"ID: {student.id}, Name: {student.name}, GPA: {self.calculate_gpa(student.id)}")
