# sams_audit_trail.py
import logging
import shutil
from datetime import datetime
 
logging.basicConfig(filename="sams_audit.log", level=logging.INFO,
                     format="%(asctime)s | %(levelname)s | %(message)s")
 
class InvalidGradeEntryError(Exception):
    pass
 
def enter_grade(roll_no, marks):
    try:
        if not (0 <= marks <= 100):
            raise InvalidGradeEntryError(f"Marks {marks} out of range for {roll_no}")
        logging.info(f"Grade entered: {roll_no} -> {marks}")
        return True
    except InvalidGradeEntryError as e:
        logging.error(str(e))
        return False
    finally:
        logging.info(f"Grade entry attempt processed for {roll_no}")
 
def backup_academic_file(source_path, backup_dir="sams_backups"):
    import os
    os.makedirs(backup_dir, exist_ok=True)
    stamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    dest = f"{backup_dir}/backup_{stamp}.bak"
    shutil.copy(source_path, dest)
    return dest
 
if __name__ == "__main__":
    print("=== SAMS Audit Trail Demo ===")
    print("Valid entry accepted:", enter_grade("SAMS24CS014", 88))
    print("Invalid entry rejected:", enter_grade("SAMS24CS099", 150))
    print("Check sams_audit.log for the full audit trail.")