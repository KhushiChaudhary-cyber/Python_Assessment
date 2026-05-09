# Program: Armstrong Number Checker
# This program checks whether a number is an Armstrong number
# using loops and conditional statements

# Take input from user
number = int(input("Enter a number: "))

# Store original number
original_number = number

# Count number of digits
digits = 0
temp = number

while temp > 0:
    digits += 1
    temp = temp // 10

# Calculate Armstrong sum
armstrong_sum = 0
temp = number

while temp > 0:
    digit = temp % 10
    armstrong_sum += digit ** digits
    temp = temp // 10

# Check condition
if armstrong_sum == original_number:
    print("\nResult: Armstrong Number")
else:
    print("\nResult: Not an Armstrong Number")
'''output:Enter a number: 56

Result: Not an Armstrong Number

output2:Enter a number: 153

Result: Armstrong Number'''