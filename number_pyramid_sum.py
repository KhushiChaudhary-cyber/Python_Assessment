# Program: Number Pyramid Pattern and Sum Calculation
# This program prints a pyramid of numbers and calculates the sum
# of all numbers printed in the pattern

# Take input from user
rows = int(input("Enter number of rows: "))

# Initialize sum
total_sum = 0

# Generate pyramid pattern
for i in range(1, rows + 1):
    # Print spaces for alignment
    for j in range(rows - i):
        print(" ", end="")

    # Print numbers in pyramid row
    for k in range(1, i + 1):
        print(k, end="")
        total_sum += k

    print()  # Move to next line

# Display total sum
print("\nSum of all numbers in pyramid:", total_sum)
'''output:

'''