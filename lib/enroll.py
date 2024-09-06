from datetime import datetime

class Student:

    all = []

    def __init__(self, name):
        self.name = name
        Student.all.append(self)

    def enroll_in_course(self, course):
        Enrollment(self, course)

    def enrollments(self):
        return [enrollment for enrollment in Enrollment.all if enrollment.student == self]

    def courses(self):
        return [enrollment.course for enrollment in self.enrollments()]

class Course:

    all = []

    def __init__(self, title):
        self.title = title
        Course.all.append(self)

    def enrollments(self):
        return [enrollment for enrollment in Enrollment.all if enrollment.course == self]

    def students(self):
        return [enrollment.student for enrollment in self.enrollments()]

    def enroll_student(self, student):
        Enrollment(student, self)

class Enrollment:

    all = []

    def __init__(self, student, course):
        self.student = student
        self.course = course
        self.enrollment_date = datetime.now()
        Enrollment.all.append(self)


# student = Student('Angel')
# course = Course('Kiswahili')

# student.enroll_in_course(course)
# print(student.enrollments()[0].enrollment_date)
# # => 2023-05-02 08:39:57.570467
# print(course.enrollments()[0].enrollment_date)
# # => 2023-05-02 08:39:57.570467
# print(student.enrollments()[0].course.title)
# # => Math 31


# Create students
student1 = Student("Alice")
student2 = Student("Bob")

# Create courses
course1 = Course("Math")
course2 = Course("Science")

# Enroll students in courses
student1.enroll_in_course(course1)
student1.enroll_in_course(course2)
student2.enroll_in_course(course1)

# Get a student's courses
print(f"{student1.name} is enrolled in the following courses:")
for course in student1.courses():
    print(course.title)

# Get students in a course
print(f"\nThe following students are enrolled in {course1.title}:")
for student in course1.students():
    print(student.name)

# Print all enrollments
print("\nAll enrollments:")
for enrollment in Enrollment.all:
    print(f"Student: {enrollment.student.name}, Course: {enrollment.course.title}, Date: {enrollment.enrollment_date}")