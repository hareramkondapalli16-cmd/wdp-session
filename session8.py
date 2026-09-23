def compute_grade_point(marks, scale=10):
    boundaries = [(90, 10), (80, 9), (70, 8), (60, 7), (50, 6), (40, 5), (0, 0)]
    for cutoff, points in boundaries:
        if marks >= cutoff:
            return points if scale == 10 else round(points * scale / 10, 2)
 
def compute_attendance_pct(present, total):
    return round((present / total) * 100, 2) if total else 0.0
 
def is_eligible(cgpa, attendance, min_cgpa=5.0, min_attendance=75):
    return cgpa >= min_cgpa and attendance >= min_attendance
 
format_currency = lambda amount: f"Rs. {amount:,.2f}"
format_percentage = lambda value: f"{value:.1f}%"
 
if __name__ == "__main__":
    print("=== SAMS Utility Library Test ===")
    print("Grade point for 84 marks:", compute_grade_point(84))
    print("Attendance %:", format_percentage(compute_attendance_pct(18, 20)))
    print("Eligible (8.2, 88):", is_eligible(8.2, 88))
    print("Formatted fee:", format_currency(45000))