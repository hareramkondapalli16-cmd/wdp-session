student_records = []
COURSE_CATALOGUE = (
    ("CS501", "Database Systems", 4),
    ("CS502", "Operating Systems", 4),
    ("CS503", "Web Development using Python", 3),
)
enrolled_students = {"CS501": set(), "CS502": set(), "CS503": set()}
faculty_course_map = {}
 
def add_student(roll_no, name):
    student_records.append({"roll_no": roll_no, "name": name})
 
def enrol_student(roll_no, course_code):
    enrolled_students[course_code].add(roll_no)
 
def assign_faculty(faculty_name, course_codes):
    faculty_course_map[faculty_name] = course_codes
 
if __name__ == "__main__":
    add_student("SAMS24CS014", "hari")
    add_student("SAMS24CS015", "ram")
    enrol_student("SAMS24CS014","CS501")
    enrol_student("SAMS24CS015","CS501")
    enrol_student("SAMS24CS014","CS503")
    assign_faculty("Dr. Rama Krishna", ["CS501", "CS502"])
 
    print("=== SAMS In-Memory Repository ===")
    print("Students:", student_records)
    print("Catalogue:", COURSE_CATALOGUE)
    print("CS501 enrolled:", enrolled_students["CS501"])
    print("Faculty map:", faculty_course_map)