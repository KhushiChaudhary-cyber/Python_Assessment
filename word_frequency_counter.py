# Program: Word Frequency Counter
# This program stores occurrence of each word from a paragraph
# into a dictionary and displays the most repeated word

# Take input from user
paragraph = input("Enter a paragraph: ")

# Convert paragraph to lowercase
paragraph = paragraph.lower()

# Remove simple punctuation marks
clean_text = ""

for ch in paragraph:
    if ch.isalnum() or ch.isspace():
        clean_text += ch

# Split paragraph into words
words = clean_text.split()

# Dictionary to store word frequency
word_count = {}

# Count frequency of each word
for word in words:
    if word in word_count:
        word_count[word] += 1
    else:
        word_count[word] = 1

# Find most repeated word
max_word = ""
max_count = 0

for word in word_count:
    if word_count[word] > max_count:
        max_count = word_count[word]
        max_word = word

# Display results
print("\nWord Frequencies:")
print(word_count)

print("\nMost Repeated Word:")
print(max_word, "->", max_count, "times")
'''output:
Enter a paragraph: this is a paragraph tpo check the word frequency

Word Frequencies:
{'this': 1, 'is': 1, 'a': 1, 'paragraph': 1, 'tpo': 1, 'check': 1, 'the': 1, 'word': 1, 'frequency': 1}

Most Repeated Word:
this -> 1 times
'''