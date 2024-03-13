import pickle
import bz2

from domains.student import *
from domains.course import *
from domains.mark import *
from input import *
from output import *

def main():
    mark_sheet = Mark()
    
    if check_students_dat():
        with bz2.BZ2File('students.dat', 'rb') as compressed_file:
            mark_sheet.students, mark_sheet.courses, mark_sheet.marks = pickle.load(compressed_file)
    else:
        num_students = input_number_of_students()
        for _ in range(num_students):
            student_info = input_student_information()
            mark_sheet.students.append(student_info)
            write_students_to_file(mark_sheet.students)

        num_courses = input_number_of_courses()
        for _ in range(num_courses):
            course_info = input_course_information()
            mark_sheet.courses.append(course_info)
            mark_sheet.marks[course_info.id] = {}
            write_courses_to_file(mark_sheet.courses)

    with bz2.BZ2File('students.dat', 'wb') as compressed_file:
        pickle.dump((mark_sheet.students, mark_sheet.courses, mark_sheet.marks), compressed_file)

    while True:
        print("\nMenu:")
        print("1. List courses")
        print("2. List students")
        print("3. Input student marks for a selected course")
        print("4. Show student marks for a selected course")
        print("5. Calculate average GPA for a given student")
        print("6. Sort students by GPA descending")
        print("7. Exit")

        choice = input("Enter your choice (1-7): ")

        if choice == '1':
            list_courses(mark_sheet.courses)
        elif choice == '2':
            list_students(mark_sheet.students)
        elif choice == '3':
            list_courses(mark_sheet.courses)
            course_id = input("Enter course ID to input marks: ")
            if course_id in [course.id for course in mark_sheet.courses]:
                print(f"Entering marks for course {course_id}:")
                course_students = mark_sheet.students  
                mark_sheet.marks[course_id] = input_student_marks(course_students)
                write_marks_to_file(mark_sheet.marks)
            else:
                print("Invalid course ID. Please select a valid course.")
        elif choice == '4':
            list_courses(mark_sheet.courses)
            course_id = input("Enter course ID to show marks: ")
            show_course_marks(course_id, mark_sheet.marks)
        elif choice == '5':
            student_id = input("Enter student ID to calculate average GPA: ")
            mark_sheet.show_student_gpa(student_id)
        elif choice == '6':
            sorted_students = mark_sheet.sort_students_by_gpa()
            show_sorted_students(sorted_students)
        elif choice == '7':
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 7.")

if __name__ == "__main__":
    main()
