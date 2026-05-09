# Program: Top Five Word Frequency from a Text File
# This program reads a text file, stores word frequencies in a dictionary,
# and displays the top five most frequently used words

try:
    # Open file for reading
    file = open("sample.txt", "r")

    # Dictionary to store word frequency
    word_count = {}

    # Read file content
    for line in file:
        # Convert to lowercase for uniformity
        line = line.lower()

        # Remove punctuation (basic cleaning)
        clean_line = ""

        for ch in line:
            if ch.isalnum() or ch.isspace():
                clean_line += ch

        # Split into words
        words = clean_line.split()

        # Count word frequency
        for word in words:
            if word in word_count:
                word_count[word] += 1
            else:
                word_count[word] = 1

    file.close()

    # Sort words by frequency (descending order)
    sorted_words = sorted(word_count.items(), key=lambda x: x[1], reverse=True)

    # Display top 5 words
    print("\nTop 5 Most Frequently Used Words:\n")

    for i in range(min(5, len(sorted_words))):
        print(sorted_words[i][0], "->", sorted_words[i][1])

# Handle file not found error
except FileNotFoundError:
    print("Error: File not found!")

# Handle other unexpected errors
except Exception as e:
    print("Unexpected error occurred:", e)
'''output:
Error: File not found!
or
Top 5 Most Frequently Used Words:
word1 -> count1
word2 -> count2
word3 -> count3
word4 -> count4
word5 -> count5
'''
