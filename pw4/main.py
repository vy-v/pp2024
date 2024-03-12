from domains.student import *
from domains.course import *
from domains.mark import *
from input import *
from output import *

def main(self):
    num_students = self.input_number_of_students()
    for _ in range(num_students):
        student_info = self.input_student_information()
        self.students.append(student_info)

    num_courses = self.input_number_of_courses()
    for _ in range(num_courses):
        course_info = self.input_course_information()
        self.courses.append(course_info)
        self.marks[course_info.id] = {} 

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
            self.list_courses()
        elif choice == '2':
            self.list_students()
        elif choice == '3':
            self.list_courses()
            course_id = input("Enter course ID to input marks: ")
            if course_id in [course.id for course in self.courses]:
                print(f"Entering marks for course {course_id}:")
                course_students = [student for student in self.students]
                self.marks[course_id] = self.input_student_marks(course_students)
            else:
                print("Invalid course ID. Please select a valid course.")
        elif choice == '4':
            self.list_courses()
            course_id = input("Enter course ID to show marks: ")

            if course_id in [course.id for course in self.courses]:
                if course_id in self.marks and self.marks[course_id]:
                    self.show_course_marks(course_id)
                else:
                    print("Marks unavailable. Please input marks for students in this course.")
            else:
                print("Invalid course ID. Please select a valid course.")
        elif choice == '5':
            student_id = input("Enter student ID to calculate average GPA: ")
            self.calculate_gpa(student_id)
            self.show_student_gpa(student_id)
        elif choice == '6':
            self.show_sorted_students()
        elif choice == '7':
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 5.")

if __name__ == "__main__":
    mark_sheet = Mark()
    mark_sheet.main()
