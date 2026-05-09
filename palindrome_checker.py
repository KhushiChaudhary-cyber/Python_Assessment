# Program: Palindrome Checker
# This program checks whether a given string is a palindrome
# after removing spaces, punctuation, and converting to lowercase

# Take input from user
text = input("Enter a string: ")

# Convert to lowercase
text = text.lower()

# Remove spaces and punctuation (keep only alphanumeric characters)
clean_text = ""

for ch in text:
    if ch.isalnum():   # checks if character is letter or digit
        clean_text += ch

# Check palindrome
if clean_text == clean_text[::-1]:
    result = "Palindrome"
else:
    result = "Not a Palindrome"

# Display result
print("\nProcessed String:", clean_text)
print("Result:", result)

'''output:
Enter a string: python is a interpreted language

Processed String: pythonisainterpretedlanguage
Result: Not a Palindrome

output2:Enter a string: madam

Processed String: madam
Result: Palindrome
'''