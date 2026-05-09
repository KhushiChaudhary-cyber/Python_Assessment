# Program: Safe Division using Function and Exception Handling
# This program divides two numbers and handles invalid inputs
# and runtime errors like division by zero

# Function for division
def divide_numbers():
    try:
        # Take input from user
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        # Perform division
        result = num1 / num2

        # Display result up to 2 decimal points
        print("\nResult of Division:", f"{result:.2f}")

    # Handle division by zero
    except ZeroDivisionError:
        print("Error: Cannot divide by zero!")

    # Handle invalid input
    except ValueError:
        print("Error: Invalid input! Please enter numeric values only.")

    # Handle any other unexpected errors
    except Exception as e:
        print("Unexpected error occurred:", e)


# Call the function
divide_numbers()
'''output:
Enter first number: 45
Enter second number: 89

Result of Division: 0.51
'''