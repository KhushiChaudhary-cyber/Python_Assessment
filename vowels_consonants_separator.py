# Program: Separate vowels and consonants from a sentence
# This program stores vowels and consonants in different lists

# Take input from user
sentence = input("Enter a sentence: ")

# Convert sentence to lowercase for uniform checking
sentence = sentence.lower()

# Lists to store vowels and consonants
vowels_list = []
consonants_list = []

# Define vowels
vowels = "aeiou"

# Loop through each character
for ch in sentence:
    if ch.isalpha():  # Check only alphabets
        if ch in vowels:
            vowels_list.append(ch)
        else:
            consonants_list.append(ch)

# Display results
print("\nVowels in the sentence:")
print(vowels_list)

print("\nConsonants in the sentence:")
print(consonants_list)
'''output:
Enter a sentence: Hello World
Vowels in the sentence:
['e', 'o', 'o']

Consonants in the sentence:
['h', 'l', 'l', 'w', 'r', 'l', 'd']
'''