# Program: Menu-driven Banking Application
# This program allows user to deposit, withdraw, check balance, and exit using a while loop

# Initialize account balance
balance = 0

# Start menu loop
while True:
    print("\n--- Banking Menu ---")
    print("1. Deposit Money")
    print("2. Withdraw Money")
    print("3. Check Balance")
    print("4. Exit")

    # Take user choice
    choice = int(input("Enter your choice (1-4): "))

    # Deposit money
    if choice == 1:
        amount = float(input("Enter amount to deposit: "))
        if amount > 0:
            balance += amount
            print("Amount deposited successfully.")
        else:
            print("Invalid amount!")

    # Withdraw money
    elif choice == 2:
        amount = float(input("Enter amount to withdraw: "))
        if amount > 0 and amount <= balance:
            balance -= amount
            print("Amount withdrawn successfully.")
        elif amount > balance:
            print("Insufficient balance!")
        else:
            print("Invalid amount!")

    # Check balance
    elif choice == 3:
        print("Current Balance:", balance)

    # Exit program
    elif choice == 4:
        print("Thank you for using the banking system.")
        break

    # Invalid choice
    else:
        print("Invalid choice! Please select between 1 and 4.")


'''output:
--- Banking Menu ---
1. Deposit Money
2. Withdraw Money
3. Check Balance
4. Exit
Enter your choice (1-4): 1
Enter amount to deposit: 5000
Amount deposited successfully.

--- Banking Menu ---
1. Deposit Money
2. Withdraw Money
3. Check Balance
4. Exit
Enter your choice (1-4): 2
Enter amount to withdraw: 34000
Insufficient balance!

--- Banking Menu ---
1. Deposit Money
2. Withdraw Money
3. Check Balance
4. Exit
Enter your choice (1-4): 3
Current Balance: 5000.0

--- Banking Menu ---
1. Deposit Money
2. Withdraw Money
3. Check Balance
4. Exit
Enter your choice (1-4): 4  
Thank you for using the banking system.'''   