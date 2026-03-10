# Simple Inventory Management System

inventory = {}

def add_product():
    name = input("Enter product name: ")
    quantity = int(input("Enter quantity: "))
    inventory[name] = quantity
    print("Product added successfully!")

def view_products():
    if not inventory:
        print("Inventory is empty.")
    else:
        print("\nCurrent Inventory:")
        for product, qty in inventory.items():
            print(f"{product}: {qty}")

def update_product():
    name = input("Enter product name to update: ")
    if name in inventory:
        quantity = int(input("Enter new quantity: "))
        inventory[name] = quantity
        print("Product updated!")
    else:
        print("Product not found.")

def remove_product():
    name = input("Enter product name to remove: ")
    if name in inventory:
        del inventory[name]
        print("Product removed!")
    else:
        print("Product not found.")

while True:
    print("\nInventory Management System")
    print("1. Add Product")
    print("2. View Products")
    print("3. Update Product")
    print("4. Remove Product")
    print("5. Exit")

    choice = input("Choose an option: ")

    if choice == "1":
        add_product()
    elif choice == "2":
        view_products()
    elif choice == "3":
        update_product()
    elif choice == "4":
        remove_product()
    elif choice == "5":
        print("Exiting system...")
        break
    else:
        print("Invalid choice")