# import re
# pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
# email = "nishananoufiya@gmail.com"
# m = re.match(pattern, email)
# print(bool(m))
# ------------------------------------------------------------------------------------
# Extract all phone numbers from a string
# import re
# pattern = r'\b(?:\+91[-\s]?)?[6-9]\d{9}\b|\b\d{3}[-\s]\d{3}[-\s]\d{4}\b'
# string = "Contact us at 9876543210 or 9123456789.You can also reach +91-9876543210 or 987-654-3210."
# phone_numbers = re.findall(pattern, string)

# print(phone_numbers)
# ---------------------------------------------------------------------------------
# Replace all occurrences of a specific word with another word.
# import re
# text = "Python is easy. Python is powerful. I love Python programming."
# pattern = r'\bPython\b'  
# replacement = "Java"
# result = re.sub(pattern, replacement, text)
# print("Original Text:")
# print(text)
# print("Updated Text:")
# print(result)

