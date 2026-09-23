def check_promotion(cgpa, attendance):
    return cgpa >= 5.0 and attendance >= 75
 
def check_scholarship(cgpa, attendance, family_income):
    return cgpa >= 8.5 and attendance >= 85 and family_income <= 600000
 
def check_probation(cgpa, attendance):
    return cgpa < 5.0 or attendance < 65
 
def eligibility_report(student):
    promoted = check_promotion(student["cgpa"], student["attendance"])
    scholarship = check_scholarship(student["cgpa"], student["attendance"], student["income"])
    probation = check_probation(student["cgpa"], student["attendance"])
 
    print(f"=== SAMS Eligibility Report: {student['roll_no']} ===")
    print(f"Promotion eligible   : {'Yes' if promoted else 'No'}")
    print(f"Scholarship eligible : {'Yes' if scholarship else 'No'}")
    print(f"Academic probation   : {'Yes - flagged' if probation else 'No'}")
 
if __name__ == "__main__":
    eligibility_report({"roll_no": "SAMS24CS014", "cgpa": 8.6, "attendance": 92, "income": 480000})
    eligibility_report({"roll_no": "SAMS24CS020", "cgpa": 4.3, "attendance": 60, "income": 350000})