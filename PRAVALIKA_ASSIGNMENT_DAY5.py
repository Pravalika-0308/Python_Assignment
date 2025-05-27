# Build a student grade management system using the following Python concepts:
# - List of dictionaries
# - Function with required arguments, *args, **kwargs
# - Function decorator
# - Loops and control statements

# Requirements
# 1. Use a **decorator** to log function activity.
# 2. Use a function to **add student data** using `*args` and `**kwargs`.
# 3. Store student records in a **list of dictionaries**.
# 4. Use **loops and conditionals** to calculate and display results.6


# Decorator to log function calls
def log_activity(func):
    def wrapper(*args, **kwargs):
        print(f"\nRunning function: {func.__name__}")
        return func(*args, **kwargs)
    return wrapper

# List to store student data
student_records = []

# Function to add student data
@log_activity
def add_student(name, roll, *marks, **details):
    student = {
        'name': name,
        'roll': roll,
        'marks': marks
    }
    for key in details:
        student[key] = details[key]
    student_records.append(student)

# Function to display student results
@log_activity
def show_results():
    for student in student_records:
        print("Name:", student['name'])
        print("Roll No:", student['roll'])
        print("Marks:", student['marks'])

        if student['marks']:
            total = sum(student['marks'])
            avg = total / len(student['marks'])

            print("Average:", round(avg, 2))

            if avg >= 90:
                print("Grade: A+")
            elif avg >= 75:
                print("Grade: A")
            elif avg >= 60:
                print("Grade: B")
            elif avg >= 50:
                print("Grade: C")
            else:
                print("Grade: F")
        else:
            print("No marks available")

# Sample students
add_student("Laxmi", 1, 85, 90, 88, age=20, branch="CSE")
add_student("Saraswathi", 2, 72, 68, 75, age=21, branch="ECE")
add_student("madhavi", 3, 45, 55, 50, age=22, branch="IT")

# Show all results
show_results()
