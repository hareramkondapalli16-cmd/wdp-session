def register_student():
    print("--- SAMS Student Registration ---")
    name = input("Full name: ").strip().title()
    roll_no = input("Roll number (e.g. SAMS24CS001): ").strip().upper()
    age = int(input("Age: "))
    cgpa = float(input("Current CGPA: "))
    fee_amount = float(input("Semester fee amount (INR): "))
 
    if not (16 <= age <= 40):
        raise ValueError("Age out of accepted range for SAMS registration.")
    if not (0.0 <= cgpa <= 10.0):
        raise ValueError("CGPA must be between 0.0 and 10.0.")
 
    return {
        "name": name, "roll_no": roll_no, "age": age,
        "cgpa": cgpa, "fee_amount": fee_amount,
    }
 
def print_summary(student):
    print("\n=== SAMS Registration Summary ===")
    print(f"Name       : {student['name']}")
    print(f"Roll No.   : {student['roll_no']}")
    print(f"Age        : {student['age']} years")
    print(f"CGPA       : {student['cgpa']:.2f}")
    print(f"Fee Amount : Rs. {student['fee_amount']:,.2f}")
 
if __name__ == "__main__":
    student = register_student()
    print_summary(student)
    