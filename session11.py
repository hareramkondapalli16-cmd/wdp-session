# sams_user_roles.py
 
class User:
    def __init__(self, user_id, name):
        self.user_id = user_id
        self.name = name
 
    def dashboard(self):
        return f"{self.name}: generic user dashboard"
 
class Student(User):
    def __init__(self, user_id, name, cgpa):
        super().__init__(user_id, name)
        self.cgpa = cgpa
 
    def dashboard(self):
        return f"{self.name}: student dashboard - CGPA {self.cgpa}, view results & attendance"
 
class Faculty(User):
    def __init__(self, user_id, name, department):
        super().__init__(user_id, name)
        self.department = department
 
    def dashboard(self):
        return f"{self.name}: faculty dashboard - {self.department}, enter grades & attendance"
 
class Administrator(User):
    def __init__(self, user_id, name):
        super().__init__(user_id, name)
        self.privileges = ["manage_users", "manage_courses", "view_all_reports"]
 
    def dashboard(self):
        return f"{self.name}: admin dashboard - privileges: {', '.join(self.privileges)}"
 
if __name__ == "__main__":
    users = [
        Student("U001", "Ananya Rao", 8.6),
        Faculty("U002", "Dr. Kavitha Menon", "Computer Science"),
        Administrator("U003", "Suresh Pillai"),
    ]
    print("=== SAMS Role-Based Dashboards (polymorphic dispatch) ===")
    for user in users:
        print(user.dashboard())