# Program: Menu-driven Mathematical Utility Program
# This program performs factorial calculation,
# prime checking, and Armstrong number checking using functions

# Function to calculate factorial
def factorial(number):
    fact = 1

    for i in range(1, number + 1):
        fact *= i

    return fact


# Function to check prime number
def is_prime(number):
    if number <= 1:
        return False

    for i in range(2, number):
        if number % i == 0:
            return False

    return True


# Function to check Armstrong number
def is_armstrong(number):
    original_number = number
    digits = len(str(number))

    armstrong_sum = 0

    while number > 0:
        digit = number % 10
        armstrong_sum += digit ** digits
        number = number // 10

    return armstrong_sum == original_number


# Menu-driven loop
while True:
    print("\n--- Mathematical Utility Program ---")
    print("1. Find Factorial")
    print("2. Check Prime Number")
    print("3. Check Armstrong Number")
    print("4. Exit")

    choice = int(input("Enter your choice (1-4): "))

    # Factorial operation
    if choice == 1:
        num = int(input("Enter a number: "))

        if num < 0:
            print("Factorial does not exist for negative numbers.")
        else:
            print("Factorial:", factorial(num))

    # Prime number check
    elif choice == 2:
        num = int(input("Enter a number: "))

        if is_prime(num):
            print(num, "is a Prime Number.")
        else:
            print(num, "is not a Prime Number.")

    # Armstrong number check
    elif choice == 3:
        num = int(input("Enter a number: "))

        if is_armstrong(num):
            print(num, "is an Armstrong Number.")
        else:
            print(num, "is not an Armstrong Number.")

    # Exit program
    elif choice == 4:
        print("Exiting program. Thank you!")
        break

    # Invalid choice
    else:
        print("Invalid choice! Please select between 1 and 4.")
        '''output:
        
--- Mathematical Utility Program ---
1. Find Factorial
2. Check Prime Number
3. Check Armstrong Number
4. Exit
Enter your choice (1-4): 1
Enter a number: 5
Factorial: 120

--- Mathematical Utility Program ---
1. Find Factorial
2. Check Prime Number
3. Check Armstrong Number
4. Exit
Enter your choice (1-4): 2
Enter a number: 34
34 is not a Prime Number.

--- Mathematical Utility Program ---
1. Find Factorial
2. Check Prime Number
3. Check Armstrong Number
4. Exit
Enter your choice (1-4): 3
Enter a number: 153
153 is an Armstrong Number.

--- Mathematical Utility Program ---
1. Find Factorial
2. Check Prime Number
3. Check Armstrong Number
4. Exit
Enter your choice (1-4): 4
Exiting program. Thank you!
        '''