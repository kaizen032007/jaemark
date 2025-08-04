import random
import mysql.connector

# Connect to MySQL
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Jaemarkalmeria#123",  # <-- Change if needed
    database="student_system"
)
cursor = db.cursor()


print("=" * 50)
print("Welcome to royal high state school")
username = input("Input your username: ")
print("-" * 50)
age = input("Input your age: ")
print("-" * 50)
email = input("Input your email: ")
print("-" * 50)
year = 25
num = str(random.randint(1000, 9999))
student_number = f"{year}-{num}"
subjects = ["Filipino", "English", "Mathematics", "Mapeh"]

errors = []

# username
if len(username) < 6:
    errors.append("Your username must contain at least 12 characters")
if " " in username:
    errors.append("Your username must not contain spaces")
if not username.isalpha():
    errors.append("Your username must not contain any numbers")

# age 
if not age.isdigit():
    errors.append("Your age must not contain any characters")
elif not (13 <= int(age) <= 24):
    errors.append("Your age must be between 13 and 24")
if " " in age:
    errors.append("Your age must not contain any spaces")

# email
if "@" not in email or "." not in email:
    errors.append("Your email must contain @ and .")

if errors:
    for error in errors:
        print(error)
else: 
    print(f"Welcome {username} to royal high state school")
    print("=" * 25)
    print("STUDENT REGISTRATION FORM")
    print("=" * 25)
    print(f"username       : {username}")
    print(f"Student Number : {student_number}")
    print("-" * 25)
    print("subjects")
    for i, subject in enumerate(subjects, start=1):
        print(f"{i}. {subject}")
    print("=" * 25)
    print("Pls proceed to the admission of Royal High estate school for the next phase")
    
    # ✅ Save to database
    insert_query = """
    INSERT INTO students (first_name, last_name, age, gender, course, email)
    VALUES (%s, %s, %s, %s, %s, %s)
    """
    values = (username, "N/A", int(age), "N/A", "N/A", email)
    cursor.execute(insert_query, values)
    db.commit()
    print("✅ Student data saved to the database!")
