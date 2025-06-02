def calculate_cgpa():
    total_credits = 0
    total_points = 0

    num_courses = int(input("Enter the number of courses: "))

    for i in range(num_courses):
        grade = input(f"Enter grade for course {i+1} (A-F): ")
        credit = int(input(f"Enter credit unit for course {i+1}: "))

        grade_points = {
            'A': 5,
            'B': 4,
            'C': 3,
            'D': 2,
            'E': 1,
            'F': 0
        }

        if grade.upper() in grade_points:
            total_points += grade_points[grade.upper()] * credit
            total_credits += credit
        else:
            print("Invalid grade. Please enter A-F.")

    if total_credits > 0:
        cgpa = total_points / total_credits
        print(f"Your CGPA is: {cgpa:.2f}")
    else:
        print("No credits earned.")

calculate_cgpa()
