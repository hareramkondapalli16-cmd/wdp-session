# Package layout:
# sams_package/
#     __init__.py
#     student.py
#     faculty.py
#     course.py
#     result.py
 
# --- sams_package/student.py ---
class Student:
    def __init__(self, roll_no, name):
        self.roll_no = roll_no
        self.name = name
 
# --- sams_package/faculty.py ---
class Faculty:
    def __init__(self, faculty_id, name):
        self.faculty_id = faculty_id
        self.name = name
 
# --- sams_package/course.py ---
class Course:
    def __init__(self, code, title):
        self.code = code
        self.title = title
 
# --- sams_package/result.py ---
def compile_result(student, marks_list):
    total = sum(marks_list)
    average = round(total / len(marks_list), 2)
    return {"roll_no": student.roll_no, "total": total, "average": average}
 
# --- sams_package/__init__.py ---
from .student import Student
from .faculty import Faculty
from .course import Course
from .result import compile_result|
 
# --- main.py (using the package) ---
from sams_package import Student, Faculty, Course, compile_result
 
if __name__ == "__main__":
    s = Student("SAMS24CS014", "Ananya Rao")
    result = compile_result(s, [88, 76, 92])
    print("=== SAMS Modular Package Test ===")
    print(f"{s.name} ({s.roll_no}) -> Total: {result['total']}, Average: {result['average']}")