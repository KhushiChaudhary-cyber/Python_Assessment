# Program: Return factorial of only even numbers from a list
# This program uses a function to filter even numbers and compute factorial

# Function to calculate factorial
def factorial(num):
    fact = 1
    for i in range(1, num + 1):
        fact = fact * i
    return fact


# Function to process list and return factorial of even numbers
def even_factorial(numbers):
    result = []

    for num in numbers:
        if num % 2 == 0:
            result.append(factorial(num))

    return result


# Take input from user
size = int(input("Enter number of elements in list: "))
num_list = []

for i in range(size):
    value = int(input(f"Enter element {i+1}: "))
    num_list.append(value)

# Call function
output = even_factorial(num_list)

# Display result
print("\nFactorial of Even Numbers:")
print(output)
'''output:
'''
