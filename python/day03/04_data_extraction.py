# 4. Data Extraction
import re
text = "Contact: 123-456-7890, email: hello@abc.com"
phones = re.findall(r'\d{3}-\d{3}-\d{4}', text)
emails = re.findall(r'[\w\.-]+@[\w\.-]+\.\w+', text)
print(phones, emails)