 
GRADE_POINTS = {"O": 10, "A+": 9, "A": 8, "B+": 7, "B": 6, "C": 5, "F": 0}
 
def classify_grade(marks):
    if marks >= 90: return "O"
    elif marks >= 80: return "A+"
    elif marks >= 70: return "A"
    elif marks >= 60: return "B+"
    elif marks >= 50: return "B"
    elif marks >= 40: return "C"
    else: return "F"
 
def compute_semester_gpa(subjects):
    total_credits = sum(c for _, c, _ in subjects)
    weighted_sum = sum(GRADE_POINTS[classify_grade(m)] * c for _, c, m in subjects)
    return round(weighted_sum / total_credits, 2)
 
def generate_grade_report(roll_no, subjects):
    print(f"=== SAMS Grade Report: {roll_no} ===")
    for name, credits, marks in subjects:
        grade = classify_grade(marks)
        print(f"{name:<20} Credits:{credits}  Marks:{marks:>3}  Grade:{grade}")
    gpa = compute_semester_gpa(subjects)
    print(f"\nSemester GPA: {gpa}")
    print("Status: PASS" if all(m >= 40 for _, _, m in subjects) else "Status: FAIL - Backlog present")
 
if __name__ == "__main__":
    subjects = [
        ("Database Systems", 4, 88),
        ("Operating Systems", 4, 76),
        ("Web Development", 3, 92),
        ("Software Engineering", 3, 55),
    ]
    generate_grade_report("SAMS24CS014", subjects)