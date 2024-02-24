class Student:
    def __init__(self, student_id, student_name, student_dob):
        self.id = student_id
        self.name = student_name
        self.dob = student_dob

class Course:
    def __init__(self, course_id, course_name):
        self.id = course_id
        self.name = course_name

class Mark:
    def __init__(self):
        self.courses = []
        self.students = []
        self.marks = {}

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
        return Course(course_id, course_name)

    def input_student_marks(self, course):
        marks_dict = {}
        for student in self.students:
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
            print("5. Exit")

            choice = input("Enter your choice (1-5): ")

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
                print("Exiting the program.")
                break
            else:
                print("Invalid choice. Please enter a number between 1 and 5.")

if __name__ == "__main__":
    mark_sheet = Mark()
    mark_sheet.main()
