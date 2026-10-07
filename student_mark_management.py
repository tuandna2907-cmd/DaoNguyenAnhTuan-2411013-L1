students = []
courses = []
marks = {}

def input_students():
    nums_student = int(input("Input number of students in a class: "))

    for num in range(nums_student):
        print(f"\nStudent {num + 1}: ")
        student_id = input("Student ID: ")
        student_name = input("Student name: ")
        student_DoB = input("Student DoB: ")

        student = {
            "id": student_id,
            "name": student_name,
            "DoB": student_DoB
        }

        students.append(student)

def input_courses():
    nums_course = int(input("Input number of courses: "))

    for num in range(nums_course):
        print(f"\nCourse {num + 1}: ")

        course_id = input("Course ID: ")
        course_name = input("Course name: ")

        course = {
            "id": course_id,
            "name": course_name
        }

        courses.append(course)

def input_marks():
    if len(courses) == 0:
        print("No courses available.")
        return

    if len(students) == 0:
        print("No students available.")
        return

    print("\n Courses List: ")

    for course in courses:
        print(f"Course ID: {course["id"]} - Name: {course["name"]}")

    course_id = input("Select your Course ID: ")

    selected_course = None

    for course in courses:
        if course["id"] == course_id:
            selected_course = course
            break

    if selected_course is None:
        print("Course not found. ")
        return

    print(f"\n Input marks for course: {selected_course["name"]}")

    if course_id not in marks:
        marks[course_id] = {}

    for student in students:
        mark = float(input(f"Input score for {student['name']}({student['id']}): "))
        marks[course_id][student['id']] = mark

def list_students():
    print("\n STUDENT LIST: ")

    for student in students:
        print(
            f"ID: {student['id']}, "
            f"Name: {student['name']}, "
            f"DoB: {student['DoB']}"
        )

def list_courses():
    print("\n COURSE LIST ")

    for course in courses:
        print(
            f"ID: {course['id']}, "
            f"Name: {course['name']} "
        )   

def show_student_marks():
    if len(courses) == 0:
        print("No courses available.")
        return

    if len(students) == 0:
        print("No students available.")
        return

    list_courses()
    course_id = input("Input course ID: ")

    selected_course = None

    for course in courses:
        if course['id'] == course_id:
            selected_course = course
            break

    if selected_course is None:
        print("Course not found. ")
        return

    print(f"\n Marks for {selected_course["name"]}: ")

    if selected_course["id"] not in marks:
        print("No marks have been entered for this course. ")
        return

    for student in students:
        print(
            f"ID: {student["id"]}, "
            f"Name: {student['name']}, "
            f"Mark: {marks[course_id][student["id"]]}"
        )

def main():
    print("\n STUDENT MARK MANAGEMENT ")

    input_students()
    input_courses()

    while True:
        print("\n========== MENU ==========")
        print("1. Input marks for a course")
        print("2. List courses")
        print("3. List students")
        print("4. Show student marks for a course")
        print("5. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            input_marks()

        elif choice == "2":
            list_courses()

        elif choice == "3":
            list_students()

        elif choice == "4":
            show_student_marks()

        elif choice == "5":
            print("Program terminated.")
            break

        else:
            print("Invalid choice. Please try again.")


main()
