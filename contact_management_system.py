# Program: Contact Management System
# This program allows users to add, update,
# search, and delete contacts using list and dictionary

# List to store contact dictionaries
contacts = []

# Function to add contact
def add_contact():
    name = input("Enter Contact Name: ")
    phone = input("Enter Phone Number: ")

    contact = {
        "Name": name,
        "Phone": phone
    }

    contacts.append(contact)
    print("Contact added successfully!")


# Function to update contact
def update_contact():
    search_name = input("Enter contact name to update: ")

    for contact in contacts:
        if contact["Name"].lower() == search_name.lower():
            new_phone = input("Enter new phone number: ")
            contact["Phone"] = new_phone
            print("Contact updated successfully!")
            return

    print("Contact not found!")


# Function to search contact
def search_contact():
    search_name = input("Enter contact name to search: ")

    for contact in contacts:
        if contact["Name"].lower() == search_name.lower():
            print("\nContact Found:")
            print("Name:", contact["Name"])
            print("Phone:", contact["Phone"])
            return

    print("Contact not found!")


# Function to delete contact
def delete_contact():
    search_name = input("Enter contact name to delete: ")

    for contact in contacts:
        if contact["Name"].lower() == search_name.lower():
            contacts.remove(contact)
            print("Contact deleted successfully!")
            return

    print("Contact not found!")


# Menu-driven system
while True:
    print("\n--- Contact Management System ---")
    print("1. Add Contact")
    print("2. Update Contact")
    print("3. Search Contact")
    print("4. Delete Contact")
    print("5. Exit")

    choice = int(input("Enter your choice (1-5): "))

    if choice == 1:
        add_contact()

    elif choice == 2:
        update_contact()

    elif choice == 3:
        search_contact()

    elif choice == 4:
        delete_contact()

    elif choice == 5:
        print("Exiting Contact Management System.")
        break

    else:
        print("Invalid choice! Please select between 1 and 5.")

        '''output:
        
--- Contact Management System ---
1. Add Contact
2. Update Contact
3. Search Contact
4. Delete Contact
5. Exit
Enter your choice (1-5): 1
Enter Contact Name: keshav
Enter Phone Number: 6789789090
Contact added successfully!

--- Contact Management System ---
1. Add Contact
2. Update Contact
3. Search Contact
4. Delete Contact
5. Exit
Enter your choice (1-5): 2
Enter contact name to update: keshav
Enter new phone number: 6789789089
Contact updated successfully!

--- Contact Management System ---
1. Add Contact
2. Update Contact
3. Search Contact
4. Delete Contact
5. Exit
Enter your choice (1-5): 3
Enter contact name to search: keshav

Contact Found:
Name: keshav
Phone: 6789789089

--- Contact Management System ---
1. Add Contact
2. Update Contact
3. Search Contact
4. Delete Contact
5. Exit
Enter your choice (1-5): 4
Enter contact name to delete: raj  
Contact not found!

--- Contact Management System ---
1. Add Contact
2. Update Contact
3. Search Contact
4. Delete Contact
5. Exit
Enter your choice (1-5): 5
Exiting Contact Management System.
        '''