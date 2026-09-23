attendance_log = {
    "Database Systems": [1, 1, 0, 1, 1, 1, 0, 1, 1, 1],
    "Operating Systems": [1, 0, 0, 1, 0, 1, 0, 1, 0, 1],
    "Web Development using Python": [1, 1, 1, 1, 1, 0, 1, 1, 1, 1],
}
 
def monthly_percentage(daily_records):
    if not daily_records:
        return 0.0
    present_days = sum(daily_records)
    return round((present_days / len(daily_records)) * 100, 2)
 
def attendance_summary():
    print("=== SAMS Subject-wise Attendance Summary ===")
    for subject, records in attendance_log.items():
        pct = monthly_percentage(records)
        status = "SHORTAGE ALERT" if pct < 75 else "OK"
        print(f"{subject:<32} {pct:>6.2f}%   [{status}]")
 
if __name__ == "__main__":
    attendance_summary()