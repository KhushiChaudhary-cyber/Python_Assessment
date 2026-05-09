# Program: Generate first N prime numbers and calculate their sum and average

# Take input from user
n = int(input("Enter how many prime numbers to generate: "))

# Validate input
while n <= 0:
    print("Invalid input! Enter a positive number.")
    n = int(input("Enter how many prime numbers to generate: "))

# List to store prime numbers
primes = []

# Starting number to check primes
num = 2

# Generate first N prime numbers
for i in range(n):
    while True:
        # Check if num is prime
        is_prime = True

        for j in range(2, num):
            if num % j == 0:
                is_prime = False
                break

        if is_prime:
            primes.append(num)
            num += 1
            break
        else:
            num += 1

# Calculate sum and average
total = sum(primes)
average = total / n

# Display results
print("\nFirst", n, "Prime Numbers:", primes)
print("Sum of Primes:", total)
print("Average of Primes:", round(average, 2))
'''output:
Enter how many prime numbers to generate: 5

First 5 Prime Numbers: [2, 3, 5, 7, 11]
Sum of Primes: 28
Average of Primes: 5.6
'''