# 3. Email Validator
import re
def validate_email(email):
    return bool(re.match(r'^[\w\.-]+@[\w\.-]+\.\w+$', email))
print(validate_email("test@example.com"))