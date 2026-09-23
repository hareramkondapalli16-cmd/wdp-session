# sams_env_check.py
import sys
import platform
 
def display_environment_info():
    print("=== SAMS Development Environment Check ===")
    print(f"Python version : {platform.python_version()}")
    print(f"Platform       : {platform.system()} {platform.release()}")
    print(f"Executable     : {sys.executable}")
    if sys.version_info < (3, 11):
        print("WARNING: SAMS requires Python 3.11 or higher.")
    else:
        print("Python version OK for SAMS development.")
 
def sams_welcome():
    print("\nWelcome to SAMS - Smart Academic Management System")
    print("EduTech Solutions Pvt. Ltd. | Skilling Lab Environment")
 
if __name__ == "__main__":
    display_environment_info()
    sams_welcome()