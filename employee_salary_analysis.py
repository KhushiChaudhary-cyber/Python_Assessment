# Program: Store employee records in tuples and display employees
# whose salary is above the average salary

# List to store employee tuples
employees = []

# Take input for number of employees
n = int(input("Enter number of employees: "))

# Input employee data
for i in range(n):
    emp_id = int(input(f"\nEnter Employee ID for employee {i+1}: "))
    emp_name = input(f"Enter Employee Name for employee {i+1}: ")
    emp_salary = float(input(f"Enter Salary for employee {i+1}: "))

    # Store data in tuple
    employee = (emp_id, emp_name, emp_salary)
    employees.append(employee)

# Calculate total salary
total_salary = 0

for emp in employees:
    total_salary += emp[2]

# Calculate average salary
average_salary = total_salary / n

# Display average salary
print("\nAverage Salary:", round(average_salary, 2))

# Display employees with salary above average
print("\nEmployees with salary above average:")

for emp in employees:
    if emp[2] > average_salary:
        print("ID:", emp[0], "| Name:", emp[1], "| Salary:", emp[2])

'''output:
Enter number of employees: 4

Enter Employee ID for employee 1: 1001
Enter Employee Name for employee 1: Josh
Enter Salary for employee 1: 340000

Enter Employee ID for employee 2: 1003
Enter Employee Name for employee 2: Kevin
Enter Salary for employee 2: 780000

Enter Employee ID for employee 3: 10005
Enter Employee Name for employee 3: Risha
Enter Salary for employee 3: 680000

Enter Employee ID for employee 4: 2004
Enter Employee Name for employee 4: Rachel
Enter Salary for employee 4: 560000

Average Salary: 590000.0

Employees with salary above average:
ID: 1003 | Name: Kevin | Salary: 780000.0
ID: 10005 | Name: Risha | Salary: 680000.0
'''        