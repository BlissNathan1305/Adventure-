from datetime import datetime

def calculate_age(birthdate):
    today = datetime.today()
    age = today.year - birthdate.year - ((today.month, today.day) < (birthdate.month, birthdate.day))
    return age

# Enter your birthdate in the format YYYY-MM-DD
birth_year = int(input("Enter your birth year: "))
birth_month = int(input("Enter your birth month (1-12): "))
birth_day = int(input("Enter your birth day (1-31): "))

birthdate = datetime(birth_year, birth_month, birth_day)

age = calculate_age(birthdate)
print(f"Your age is: {age}")
