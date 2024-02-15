class Student:
    def __init__(self, id, name, dob):
        self._id = id
        self._name = name
        self._dob = dob

    def input(self):
        self._id = input("Enter student ID: ")
        self._name = input("Enter student name: ")
        self._dob = input("Enter student Date of Birth (DoB): ")

    def __str__(self):
        return f"ID: {self._id}, Name: {self._name}, DoB: {self._dob}"

class Course:
    def __init__(self, id, name):
        self._id = id
        self._name = name

    def input(self):
        self._id = input("Enter course ID: ")
        self._name = input("Enter course name: ")

    def __str__(self):
        return f"ID: {self._id}, Name: {self._name}"

class Marks:
    def __init__(self, course_id, student_id, mark):
        self._course_id = course_id
        self._student_id = student_id
        self._mark = mark

    def __str__(self):
        return f"Course ID: {self._course_id}, Student ID: {self._student_id}, Mark: {self._mark}"

class SchoolManagementSystem:
    def __init__(self):
        self.students = []
        self.courses = []
        self.marks = []

    def input_number_of_students(self):
        num_students = int(input("Enter the number of students in the class: "))
        for _ in range(num_students):
            student = Student(None, None, None)
            student.input()
            self.students.append(student)

    def input_number_of_courses(self):
        num_courses = int(input("Enter the number of courses: "))
        for _ in range(num_courses):
            course = Course(None, None)
            course.input()
            self.courses.append(course)

    def select_course_and_input_marks(self):
        self.list_courses()
        course_id = input("Select a course by ID to input marks: ")
        for student in self.students:
            mark = float(input(f"Enter mark for student {student._name} (ID: {student._id}): "))
            self.marks.append(Marks(course_id, student._id, mark))

    def list_courses(self):
        print("Courses:")
        for course in self.courses:
            print(course)

    def list_students(self):
        print("Students:")
        for student in self.students:
            print(student)

    def show_student_marks_for_a_given_course(self):
        self.list_courses()
        course_id = input("Select a course by ID to view marks: ")
        for mark in self.marks:
            if mark._course_id == course_id:
                print(mark)

    def run(self):
        self.input_number_of_students()
        self.input_number_of_courses()
        self.select_course_and_input_marks()
        self.list_students()
        self.list_courses()
        self.show_student_marks_for_a_given_course()

if __name__ == "__main__":
    sms = SchoolManagementSystem()
    sms.run()
