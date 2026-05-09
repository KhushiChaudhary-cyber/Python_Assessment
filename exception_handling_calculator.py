# Program: Calculator with Exception Handling
# This program handles division by zero, invalid inputs,
# and incorrect operations using multiple exception blocks

try:
    # Take inputs from user
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))

    print("\nOperations: +  -  *  /")
    operator = input("Enter operation: ")

    # Perform operation based on user choice
    if operator == "+":
        result = num1 + num2
    elif operator == "-":
        result = num1 - num2
    elif operator == "*":
        result = num1 * num2
    elif operator == "/":
        result = num1 / num2   # may raise ZeroDivisionError
    else:
        raise ValueError("Invalid operator selected!")

    print("\nResult:", result)

# Handle division by zero
except ZeroDivisionError:
    print("Error: Cannot divide by zero!")

# Handle invalid numeric input
except ValueError as ve:
    print("Error:", ve)

# Handle any other unexpected errors
except Exception as e:
    print("Unexpected error occurred:", e)

# Finally block
finally:
    print("\nProgram execution completed.")
'''output:
Enter first number: 10
Enter second number: 45

Operations: +  -  *  /
Enter operation: * 

Result: 450.0

Program execution completed.
'''    