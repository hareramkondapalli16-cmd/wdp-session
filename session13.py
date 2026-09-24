# sams_json_regex.py
import json
import re
from datetime import datetime
 
EMAIL_PATTERN = r'^[\w.\-]+@[\w\-]+\.[a-zA-Z]{2,}$'
PHONE_PATTERN = r'^[6-9]\d{9}$'
ROLL_PATTERN = r'^SAMS\d{2}[A-Z]{2}\d{3}$'
 
sample_json = '''
[
  {"name": "Ananya Rao", "roll_no": "SAMS24CS014", "email": "ananya.rao@edutech.edu", "phone": "9876543210"},
  {"name": "Zoya Khan", "roll_no": "SAMS24CS099", "email": "bad-email", "phone": "12345"}
]
'''
 
def parse_admissions(json_text):
    return json.loads(json_text)
 
def validate_record(record):
    return {
        "name": record["name"],
        "roll_no_valid": bool(re.match(ROLL_PATTERN, record["roll_no"])),
        "email_valid": bool(re.match(EMAIL_PATTERN, record["email"])),
        "phone_valid": bool(re.match(PHONE_PATTERN, record["phone"])),
        "imported_at": datetime.utcnow().isoformat(timespec="seconds"),
    }
 
if __name__ == "__main__":
    records = parse_admissions(sample_json)
    print("=== SAMS External Data Validation ===")
    for r in records:
        result = validate_record(r)
        print(result)