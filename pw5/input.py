import os
from domains.student import Student
from domains.course import Course

def input_number_of_students():
    number_of_students = -1  
    while number_of_students < 0:
        user_input = input("Enter the number of students in the class: ")
        if user_input.isdigit():
            number_of_students = int(user_input)
        else:
            print("Please enter a valid number.")
    return number_of_students

def input_student_information():
    student_id = input("Enter student ID: ")
    student_name = input("Enter student name: ")
    student_dob = input("Enter student date of birth: ")
    return Student(student_id, student_name, student_dob)

def write_students_to_file(students):
    with open('students.txt', 'w') as file:
        for student in students:
            file.write(f"{student.id},{student.name},{student.dob}\n")

def input_number_of_courses():
    number_of_courses = -1  
    while number_of_courses < 0:
        user_input = input("Enter the number of courses: ")
        if user_input.isdigit():
            number_of_courses = int(user_input)
        else:
            print("Please enter a valid number.")
    return number_of_courses

def input_course_information():
    course_id = input("Enter course ID: ")
    course_name = input("Enter course name: ")
    course_credits = input("Enter course credits: ")
    return Course(course_id, course_name, int(course_credits))

def write_courses_to_file(courses):
    with open('courses.txt', 'w') as file:
        for course in courses:
            file.write(f"{course.id},{course.name},{course.credits}\n")

def input_student_marks(students):
    marks_dict = {}
    for student in students:
        student_id = student.id
        while True:
            user_input = input(f"Enter mark for {student.name} (between 0 and 20): ")
            if user_input.replace('.', '').isnumeric():
                mark = float(user_input)
                if 0 <= mark <= 20:
                    marks_dict[student_id] = mark
                    break
                else:
                    print("Please enter a valid mark between 0 and 20.")
            else:
                print("Please enter a valid value for the mark.")
    return marks_dict

def write_marks_to_file(marks):
    with open('marks.txt', 'w') as file:
        for course_id, course_marks in marks.items():
            file.write(f"Course ID: {course_id}\n")
            for student_id, mark in course_marks.items():
                file.write(f"Student ID: {student_id}, Mark: {mark}\n")

def check_students_dat():
    return os.path.exists('students.dat')
