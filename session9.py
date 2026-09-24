# sams_analytics_engine.py
from functools import reduce
 
students = [
    {"roll_no": "SAMS24CS014", "name": "Ananya Rao", "cgpa": 8.6, "attendance": 92},
    {"roll_no": "SAMS24CS015", "name": "Rohit Verma", "cgpa": 7.1, "attendance": 78},
    {"roll_no": "SAMS24CS016", "name": "Divya Iyer", "cgpa": 9.2, "attendance": 95},
    {"roll_no": "SAMS24CS017", "name": "Karan Shah", "cgpa": 4.8, "attendance": 60},
]
 
def eligible_for_honours(students):
    return list(filter(lambda s: s["cgpa"] >= 8.0 and s["attendance"] >= 85, students))
 
def class_average_cgpa(students):
    total = reduce(lambda acc, s: acc + s["cgpa"], students, 0)
    return round(total / len(students), 2)
 
def topper_list(students, top_n=2):
    ranked = sorted(students, key=lambda s: s["cgpa"], reverse=True)
    return list(map(lambda s: (s["name"], s["cgpa"]), ranked[:top_n]))
 
if __name__ == "__main__":
    print("=== SAMS Analytics Engine ===")
    print("Honours-eligible:", [s["name"] for s in eligible_for_honours(students)])
    print("Class average CGPA:", class_average_cgpa(students))
    print("Toppers:", topper_list(students))