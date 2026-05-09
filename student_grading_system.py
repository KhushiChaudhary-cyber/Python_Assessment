# Program: Student Grading System with Validation and Formatted Output
# This program takes marks of five subjects, validates input,
# calculates percentage (up to 2 decimal places),
# assigns grade using nested if-else, and checks scholarship eligibility

# Function to validate marks between 0 and 100
def get_valid_marks(subject_name):
    marks = int(input(f"Enter marks for {subject_name}: "))

    while marks < 0 or marks > 100:
        print("Invalid input! Marks must be between 0 and 100.")
        marks = int(input(f"Re-enter marks for {subject_name}: "))

    return marks


# Input marks with validation
sub1 = get_valid_marks("Subject 1")
sub2 = get_valid_marks("Subject 2")
sub3 = get_valid_marks("Subject 3")
sub4 = get_valid_marks("Subject 4")
sub5 = get_valid_marks("Subject 5")

# Calculate total and percentage
total_marks = sub1 + sub2 + sub3 + sub4 + sub5
percentage = (total_marks / 500) * 100

# Grade assignment using nested if-else
if percentage >= 90:
    grade = "A+"
    scholarship = "Yes"
elif percentage >= 75:
    grade = "A"
    if percentage >= 80:
        scholarship = "Yes"
    else:
        scholarship = "No"
elif percentage >= 60:
    grade = "B"
    scholarship = "No"
elif percentage >= 40:
    grade = "C"
    scholarship = "No"
else:
    grade = "Fail"
    scholarship = "No"

# Display results
print("\n--- Result ---")
print("Total Marks:", total_marks, "/ 500")
print("Percentage:", f"{percentage:.2f}", "%")
print("Grade:", grade)
print("Scholarship Eligible:", scholarship)
'''output:
Enter marks for Subject 1: 67
Enter marks for Subject 2: 89
Enter marks for Subject 3: 99
Enter marks for Subject 4: 57
Enter marks for Subject 5: 77

--- Result ---
Total Marks: 389 / 500
Percentage: 77.80 %
Grade: A
Scholarship Eligible: No'''