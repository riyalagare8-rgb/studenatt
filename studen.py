# eligibility-check: Attendance Percentage and Exam Eligibility

def calculate_attendance(classes_held, classes_attended):
    if classes_held == 0:
        return 0  # Avoid division by zero
    percentage = (classes_attended / classes_held) * 100
    return percentage

def check_eligibility(percentage):
    return percentage >= 75

# Input from user
try:
    held = int(input("Enter the number of classes held: "))
    attended = int(input("Enter the number of classes attended: "))

    if held < 0 or attended < 0:
        print("Class counts cannot be negative.")
    elif attended > held:
        print("Classes attended cannot exceed classes held.")
    else:
        attendance = calculate_attendance(held, attended)
        print(f"Attendance Percentage: {attendance:.2f}%")

        if check_eligibility(attendance):
            print("✅ Eligible for Exams")
        else:
            print("❌ Not Eligible for Exams (Minimum 75% required)")
except ValueError:
    print("Invalid input. Please enter whole numbers.")