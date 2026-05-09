# Program: File Processing with Exception Handling
# This program reads a text file and counts:
# total words, lines, and characters
# It also handles file not found errors

try:
    # Take filename from user
    file_name = input("Enter file name (with extension): ")

    # Open file in read mode
    file = open(file_name, "r")

    # Initialize counters
    line_count = 0
    word_count = 0
    char_count = 0

    # Read file line by line
    for line in file:
        line_count += 1
        char_count += len(line)
        words = line.split()
        word_count += len(words)

    file.close()

    # Display results
    print("\n--- File Analysis ---")
    print("Total Lines:", line_count)
    print("Total Words:", word_count)
    print("Total Characters:", char_count)

# Handle file not found error
except FileNotFoundError:
    print("Error: File not found! Please check the filename.")

# Handle other unexpected errors
except Exception as e:
    print("Unexpected error occurred:", e)

'''output:
Enter file name (with extension): sample.txt
Error: File not found! Please check the filename.
'''   