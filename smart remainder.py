import re

patient_id = input("Enter Patient ID: ")
name = input("Enter Name: ")
age = int(input("Enter Age: "))
gender = input("Enter Gender: ")
phone = input("Enter Phone Number: ")
email = input("Enter Email: ")

if not patient_id:
    print("Invalid Patient ID")
elif not name.replace(" ", "").isalpha():
    print("Invalid Name")
elif age < 0 or age > 120:
    print("Invalid Age")
elif gender not in ["Male", "Female", "Other"]:
    print("Invalid Gender")
elif len(phone) != 10 or not phone.isdigit():
    print("Invalid Phone Number")
elif not re.match(r'^[\w\.-]+@[\w\.-]+\.\w+$', email):
    print("Invalid Email")
else:
    print("Patient Record Validated Successfully")
