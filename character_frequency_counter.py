# Program to count uppercase, lowercase, digits, spaces, and special characters

# Take input from user
text = input("Enter a paragraph: ")

# Initialize counters
uppercase = 0
lowercase = 0
digits = 0
spaces = 0
special = 0

# Loop through each character in the text
for ch in text:
    if ch.isupper():
        uppercase += 1
    elif ch.islower():
        lowercase += 1
    elif ch.isdigit():
        digits += 1
    elif ch.isspace():
        spaces += 1
    else:
        special += 1

# Store results in a list for sorting
results = [
    ("Uppercase Letters", uppercase),
    ("Lowercase Letters", lowercase),
    ("Digits", digits),
    ("Spaces", spaces),
    ("Special Characters", special)
]

# Sort in descending order based on count
results.sort(key=lambda x: x[1], reverse=True)

# Display results
print("\nCharacter Frequency (Descending Order):")
for item in results:
    print(item[0], ":", item[1])
'''output:Enter a paragraph: this is python 

Character Frequency (Descending Order):
Lowercase Letters : 12
Spaces : 3
Uppercase Letters : 0
Digits : 0
Special Characters : 0'''    