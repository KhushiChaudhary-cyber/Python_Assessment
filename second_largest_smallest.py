# Program: Find second largest and second smallest element in a list
# without using built-in sorting functions

# Function to find second largest and second smallest
def find_second_elements(numbers):
    # Remove duplicates to handle repeated values
    unique_numbers = []

    for num in numbers:
        if num not in unique_numbers:
            unique_numbers.append(num)

    # Check if enough elements exist
    if len(unique_numbers) < 2:
        return None, None

    # Initialize variables
    largest = second_largest = float('-inf')
    smallest = second_smallest = float('inf')

    # Find largest and smallest first
    for num in unique_numbers:
        if num > largest:
            largest = num
        if num < smallest:
            smallest = num

    # Find second largest and second smallest
    for num in unique_numbers:
        if num != largest and num > second_largest:
            second_largest = num
        if num != smallest and num < second_smallest:
            second_smallest = num

    return second_largest, second_smallest


# Input list from user
size = int(input("Enter number of elements in list: "))
numbers_list = []

for i in range(size):
    value = int(input(f"Enter element {i+1}: "))
    numbers_list.append(value)

# Call function
sec_largest, sec_smallest = find_second_elements(numbers_list)

# Display result
if sec_largest is None:
    print("Not enough unique elements to find second largest and second smallest.")
else:
    print("\nSecond Largest Element:", sec_largest)
    print("Second Smallest Element:", sec_smallest)
'''output:
Enter number of elements in list: 5
Enter element 1: 34
Enter element 2: 56
Enter element 3: 78
Enter element 4: 88
Enter element 5: 1

Second Largest Element: 78
Second Smallest Element: 34
    '''