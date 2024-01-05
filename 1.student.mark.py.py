students = []
courses = []
marks = {}

def input_number_of_students():
    return int(input("Enter the number of students in the class: "))

def input_student_information():
    id = input("Enter student ID: ")
    name = input("Enter student name: ")
    dob = input("Enter student Date of Birth (DoB): ")
    students.append({"id": id, "name": name, "dob": dob})

def input_number_of_courses():
    return int(input("Enter the number of courses: "))

def input_course_information():
    id = input("Enter course ID: ")
    name = input("Enter course name: ")
    courses.append({"id": id, "name": name})

def select_course_and_input_marks():
    list_courses()
    course_id = input("Select a course by ID to input marks: ")
    selected_course = next((course for course in courses if course["id"] == course_id), None)
    if selected_course:
        for student in students:
            mark = float(input(f"Enter mark for student {student['name']} (ID: {student['id']}): "))
            marks.setdefault(course_id, []).append({"student_id": student["id"], "mark": mark})
    else:
        print("Course not found!")

def list_courses():
    print("Courses:")
    for course in courses:
        print(f"ID: {course['id']}, Name: {course['name']}")

def list_students():
    print("Students:")
    for student in students:
        print(f"ID: {student['id']}, Name: {student['name']}, DoB: {student['dob']}")

def show_student_marks_for_a_given_course():
    list_courses()
    course_id = input("Select a course by ID to view marks: ")
    if course_id in marks:
        print(f"Marks for Course ID: {course_id}")
        for record in marks[course_id]:
            student = next(student for student in students if student["id"] == record["student_id"])
            print(f"Student: {student['name']} (ID: {student['id']}), Mark: {record['mark']}")
    else:
        print("No marks found for this course or course does not exist.")

def main():
    num_students = input_number_of_students()
    for _ in range(num_students):
        input_student_information()

    num_courses = input_number_of_courses()
    for _ in range(num_courses):
        input_course_information()

    select_course_and_input_marks()

    list_students()
    list_courses()
    show_student_marks_for_a_given_course()

if __name__ == "__main__":
    main()