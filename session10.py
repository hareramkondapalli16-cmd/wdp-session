# sams_domain_model.py
 
class Student:
    def __init__(self, roll_no, name, cgpa):
        self.roll_no = roll_no
        self.name = name
        self.cgpa = cgpa
        self.enrolled_courses = []
 
    def enrol(self, course):
        self.enrolled_courses.append(course)
        course.enrolled_students.append(self)
 
    def display_profile(self):
        courses = ", ".join(c.code for c in self.enrolled_courses) or "None"
        print(f"{self.roll_no} | {self.name} | CGPA {self.cgpa} | Courses: {courses}")
 
class Faculty:
    def __init__(self, faculty_id, name):
        self.faculty_id = faculty_id
        self.name = name
        self.courses_taught = []
 
    def assign_course(self, course):
        self.courses_taught.append(course)
        course.faculty = self
 
class Course:
    def __init__(self, code, title, credits):
        self.code = code
        self.title = title
        self.credits = credits
        self.enrolled_students = []
        self.faculty = None
 
if __name__ == "__main__":
    cs501 = Course("CS501", "Database Systems", 4)
    faculty = Faculty("F001", "Dr. Kavitha Menon")
    faculty.assign_course(cs501)
 
    student = Student("SAMS24CS014", "Ananya Rao", 8.6)
    student.enrol(cs501)
 
    print("=== SAMS OOP Domain Model ===")
    student.display_profile()
    print(f"{cs501.code} taught by {cs501.faculty.name}, {len(cs501.enrolled_students)} student(s) enrolled")