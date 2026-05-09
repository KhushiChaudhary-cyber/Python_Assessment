# Program: Generate Fibonacci numbers up to N and store even Fibonacci numbers
# This program uses functions and loops

# Function to generate Fibonacci series and filter even numbers
def even_fibonacci(n):
    fib_even_list = []

    a = 0
    b = 1

    for i in range(n):
        fib_next = a + b
        a = b
        b = fib_next

        # Check if Fibonacci number is even
        if fib_next % 2 == 0:
            fib_even_list.append(fib_next)

    return fib_even_list


# Take input from user
n = int(input("Enter number of Fibonacci terms: "))

# Validate input
while n <= 0:
    print("Invalid input! Enter a positive number.")
    n = int(input("Enter number of Fibonacci terms: "))

# Call function
even_fib_numbers = even_fibonacci(n)

# Display result
print("\nEven Fibonacci Numbers:")
print(even_fib_numbers)
'''output:
Enter number of Fibonacci terms: 34

Even Fibonacci Numbers:
[2, 8, 34, 144, 610, 2584, 10946, 46368, 196418, 832040, 3524578]
'''