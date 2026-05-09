# Program: Merge two lists, remove duplicates, sort in descending order,
# and display numbers divisible by both 3 and 5

# Take input for first list
size1 = int(input("Enter number of elements in List 1: "))
list1 = []

for i in range(size1):
    value = int(input(f"Enter element {i+1} of List 1: "))
    list1.append(value)

# Take input for second list
size2 = int(input("\nEnter number of elements in List 2: "))
list2 = []

for i in range(size2):
    value = int(input(f"Enter element {i+1} of List 2: "))
    list2.append(value)

# Merge both lists
merged_list = list1 + list2

# Remove duplicates
unique_list = []

for num in merged_list:
    if num not in unique_list:
        unique_list.append(num)

# Sort in descending order
for i in range(len(unique_list)):
    for j in range(i + 1, len(unique_list)):
        if unique_list[i] < unique_list[j]:
            unique_list[i], unique_list[j] = unique_list[j], unique_list[i]

# Filter numbers divisible by both 3 and 5
result_list = []

for num in unique_list:
    if num % 3 == 0 and num % 5 == 0:
        result_list.append(num)

# Display results
print("\nMerged Unique Sorted List (Descending):", unique_list)
print("Numbers divisible by both 3 and 5:", result_list)
'''output:
Enter number of elements in List 1: 4
Enter element 1 of List 1: 34
Enter element 2 of List 1: 45
Enter element 3 of List 1: 2
Enter element 4 of List 1: 33

Enter number of elements in List 2: 5
Enter element 1 of List 2: 33
Enter element 2 of List 2: 4
Enter element 3 of List 2: 22
Enter element 4 of List 2: 5
Enter element 5 of List 2: 67

Merged Unique Sorted List (Descending): [67, 45, 34, 33, 22, 5, 4, 2]
Numbers divisible by both 3 and 5: [45]
'''