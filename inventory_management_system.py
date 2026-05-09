# Program: Dictionary-based Inventory Management System
# This program allows adding products, updating quantity,
# searching products, and displaying low-stock items

# Inventory dictionary
inventory = {}

# Function to add product
def add_product():
    product_id = input("Enter Product ID: ")

    if product_id in inventory:
        print("Product already exists!")
    else:
        name = input("Enter Product Name: ")
        quantity = int(input("Enter Quantity: "))
        inventory[product_id] = [name, quantity]
        print("Product added successfully!")

# Function to update quantity
def update_quantity():
    product_id = input("Enter Product ID to update: ")

    if product_id in inventory:
        new_qty = int(input("Enter new quantity: "))
        inventory[product_id][1] = new_qty
        print("Quantity updated successfully!")
    else:
        print("Product not found!")

# Function to search product
def search_product():
    product_id = input("Enter Product ID to search: ")

    if product_id in inventory:
        print("Product Found:")
        print("Name:", inventory[product_id][0])
        print("Quantity:", inventory[product_id][1])
    else:
        print("Product not found!")

# Function to display low stock items
def low_stock():
    threshold = int(input("Enter low stock threshold: "))

    print("\nLow Stock Items:")
    found = False

    for pid, details in inventory.items():
        if details[1] <= threshold:
            print("ID:", pid, "| Name:", details[0], "| Quantity:", details[1])
            found = True

    if not found:
        print("No low stock items found.")

# Menu-driven system
while True:
    print("\n--- Inventory Management System ---")
    print("1. Add Product")
    print("2. Update Quantity")
    print("3. Search Product")
    print("4. Display Low Stock Items")
    print("5. Exit")

    choice = int(input("Enter your choice (1-5): "))

    if choice == 1:
        add_product()
    elif choice == 2:
        update_quantity()
    elif choice == 3:
        search_product()
    elif choice == 4:
        low_stock()
    elif choice == 5:
        print("Exiting system. Thank you!")
        break
    else:
        print("Invalid choice! Please select 1-5.")
'''output:
--- Inventory Management System ---
1. Add Product
2. Update Quantity
3. Search Product
4. Display Low Stock Items
5. Exit
Enter your choice (1-5): 1
Enter Product ID: 2003
Enter Product Name: Mobile           
Enter Quantity: 4 
Product added successfully!

--- Inventory Management System ---
1. Add Product
2. Update Quantity
3. Search Product
4. Display Low Stock Items
5. Exit
Enter your choice (1-5): 2
Enter Product ID to update: 2003
Enter new quantity: 6
Quantity updated successfully!

--- Inventory Management System ---
1. Add Product
2. Update Quantity
3. Search Product
4. Display Low Stock Items
5. Exit
Enter your choice (1-5): 1
Enter Product ID: 4005
Enter Product Name: laptop
Enter Quantity: 34
Product added successfully!

--- Inventory Management System ---
1. Add Product
2. Update Quantity
3. Search Product
4. Display Low Stock Items
5. Exit
Enter your choice (1-5): 1
Enter Product ID: 3007
Enter Product Name: Smartphone
Enter Quantity: 35
Product added successfully!

--- Inventory Management System ---
1. Add Product
2. Update Quantity
3. Search Product
4. Display Low Stock Items
5. Exit
Enter your choice (1-5): 3
Enter Product ID to search: 3007
Product Found:
Name: Smartphone
Quantity: 35

--- Inventory Management System ---
1. Add Product
2. Update Quantity
3. Search Product
4. Display Low Stock Items
5. Exit
Enter your choice (1-5): 4
Enter low stock threshold: 4

Low Stock Items:
No low stock items found.

--- Inventory Management System ---
1. Add Product
2. Update Quantity
3. Search Product
4. Display Low Stock Items
5. Exit
Enter your choice (1-5): 5
Exiting system. Thank you!
 '''       