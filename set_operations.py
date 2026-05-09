# Program: Set Operations (Union, Intersection, Symmetric Difference, Subset)
# This program performs basic set operations on two user-defined sets

# Take input for first set
n1 = int(input("Enter number of elements in Set A: "))
set_a = set()

for i in range(n1):
    value = int(input(f"Enter element {i+1} of Set A: "))
    set_a.add(value)

# Take input for second set
n2 = int(input("\nEnter number of elements in Set B: "))
set_b = set()

for i in range(n2):
    value = int(input(f"Enter element {i+1} of Set B: "))
    set_b.add(value)

# Perform set operations
union_set = set_a | set_b
intersection_set = set_a & set_b
symmetric_diff_set = set_a ^ set_b

# Check subset condition
is_subset_a_b = set_a.issubset(set_b)
is_subset_b_a = set_b.issubset(set_a)

# Display results
print("\n--- Set Operations Result ---")
print("Set A:", set_a)
print("Set B:", set_b)

print("\nUnion:", union_set)
print("Intersection:", intersection_set)
print("Symmetric Difference:", symmetric_diff_set)

print("\nIs Set A subset of Set B?:", is_subset_a_b)
print("Is Set B subset of Set A?:", is_subset_b_a)

'''output::
Enter number of elements in Set A: 3 
Enter element 1 of Set A: 6967
Enter element 2 of Set A: 45
Enter element 3 of Set A: 44

Enter number of elements in Set B: 4
Enter element 1 of Set B: 67
Enter element 2 of Set B: 887
Enter element 3 of Set B: 65
Enter element 4 of Set B: 567

--- Set Operations Result ---
Set A: {44, 45, 6967}
Set B: {65, 67, 567, 887}

Union: {65, 67, 567, 6967, 44, 45, 887}
Intersection: set()
Symmetric Difference: {65, 67, 44, 45, 6967, 887, 567}

Is Set A subset of Set B?: False
Is Set B subset of Set A?: False'''