import random

username = input("Type your username: ")
age = input("Type your age: ")
email = input("Type your email: ")
digits = [str(random.randint(0, 9)) for _ in range(16)]
card_number = (
    "".join(digits[0:4]) + "-" +
    "".join(digits[4:8]) + "-" +
    "".join(digits[8:12]) + "-" +
    "".join(digits[12:16])
)

errors = []

# username 
if len(username) < 12:
    errors.append("Your username must contain at least 12 characters")
if not username.isalpha():
    errors.append("Your username must not contain any number")
if " " in username:
    errors.append("Your username must not contain any spaces")

# age
if not age.isdigit():
    errors.append("Your age must not contain any letters")
elif not (18 <= int(age) <= 99):
    errors.append("You must be 18 or above")
if " " in age:
    errors.append("Your age must not contain any spaces")

# email
if "@" not in email or "." not in email:
    errors.append("Your email must contain @ and .")

    
if errors:
    for error in errors:
        print(error)
else:
    print(f"Welcome {username} to the high rise banking. Here is your new bank account card number: {card_number}")