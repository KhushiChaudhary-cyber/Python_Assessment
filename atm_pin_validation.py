# Program: ATM PIN Validation System
# This program validates ATM PIN and locks the account
# after three invalid attempts

# Correct ATM PIN
correct_pin = "1234"

# Counter for invalid attempts
attempts = 0

# Maximum allowed attempts
max_attempts = 3

# Loop for PIN validation
while attempts < max_attempts:

    # Take PIN input from user
    entered_pin = input("Enter your ATM PIN: ")

    # Check PIN
    if entered_pin == correct_pin:
        print("\nPIN verified successfully!")
        print("Access Granted.")
        break

    else:
        attempts += 1
        remaining = max_attempts - attempts

        print("\nInvalid PIN!")

        # Show remaining attempts
        if remaining > 0:
            print("Remaining Attempts:", remaining)

# Lock account after 3 invalid attempts
if attempts == max_attempts:
    print("\nAccount Locked due to 3 invalid attempts.")
    '''output:
   Enter your ATM PIN: 1111

Invalid PIN!
Remaining Attempts: 2
Enter your ATM PIN: 12345

Invalid PIN!
Remaining Attempts: 1
Enter your ATM PIN: 12

Invalid PIN!

Account Locked due to 3 invalid attempts.


output2:
Enter your ATM PIN: 1234
PIN verified successfully!
Access Granted.

    '''