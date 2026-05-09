# Program: Sum of Digits using Recursive and Iterative Approach
# This program calculates the sum of digits of a number
# using both recursion and iteration

# Recursive function
def recursive_sum(number):

    # Base condition
    if number == 0:
        return 0

    # Recursive case
    return (number % 10) + recursive_sum(number // 10)


# Iterative function
def iterative_sum(number):

    total = 0

    while number > 0:
        digit = number % 10
        total += digit
        number = number // 10

    return total


# Take input from user
num = int(input("Enter a number: "))

# Handle negative numbers
if num < 0:
    num = abs(num)

# Calculate sums
recursive_result = recursive_sum(num)
iterative_result = iterative_sum(num)

# Display results
print("\nSum using Recursive Approach:", recursive_result)
print("Sum using Iterative Approach:", iterative_result)

# Compare results
if recursive_result == iterative_result:
    print("\nBoth approaches give the same result.")
else:
    print("\nResults are different.")
'''output:

Enter a number: 12345
Sum using Recursive Approach: 15
Sum using Iterative Approach: 15
Both approaches give the same result.
Enter a number: -987
Sum using Recursive Approach: 24
Sum using Iterative Approach: 24
Both approaches give the same result.
'''
