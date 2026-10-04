import json
import os


def data_representation():
    print("==================================================")
    print("INVENTORY MANAGEMENT SYSTEM")
    print("==================================================\n")

    if os.path.exists("inventory.json"):
        with open("inventory.json", "r") as file:
            inventory = json.load(file)
            print("inventory.json found")
            print("Inventory loaded successfully.\n")

       # with open("inventory.json", "r") as file: #read the file and print the data
       #     data = json.load(file)
       #     print(data)
    else:
        print("inventory.json not found. Creating a new inventory file...")
        with open("inventory.json", "w") as file:
            json.dump([
    {
        "ID": "P001",
        "Name": "Laptop",
        "Price": "$1200",
        "Stock": 50
    },
    {
        "ID": "P002",
        "Name": "Mouse",
        "Price": "$25.50",
        "Stock": 30
    },
    {
        "ID": "P003",
        "Name": "Keyboard",
        "Price": "$45.00",
        "Stock": 20
    }], file)
            print("New inventory file created successfully.\n")

    print("--------------MENU---------------")
    print("1. Display All Products")
    print("2. Add Product")
    print("3. Update Product")
    print("4. Search Product")
    print("5. Save Inventory")
    print("6. Exit")
    print("---------------------------------\n")


def option_1():
    with open("inventory.json", "r") as file:
        inventory = json.load(file)
        for product in inventory:
            print(f"ID: {product['ID']} | Name: {product['Name']} | Price: {product['Price']} | Stock: {product['Stock']}")
        print()
    options()

def option_2():

    print("Add New Product")
    with open("inventory.json", "r") as file:
        inventory = json.load(file)

    product_id = input("Product ID: ")
    product_name = input("Product Name: ")
    product_price = input("Price: ")
    product_stock = int(input("Stock Quantity: "))

    new_product = {
        "ID": product_id,
        "Name": product_name,
        "Price": product_price,
        "Stock": product_stock
    }

    inventory.append(new_product)

    with open("inventory.json", "w") as file:
        json.dump(inventory, file, indent=4)

    print("Product added successfully.\n")
    options()

def option_3():
    print("Update Stock")
    with open("inventory.json", "r") as file:
        inventory = json.load(file)

    product_id = input("Enter Product ID: ")
    for product in inventory:
        if product["ID"] == product_id:
            print("\nProduct Found")
            print(f"Name: {product['Name']}\nStock: {product['Stock']}\n")
            new_stock_quantity = input("New stock quantity: ")
            product["Stock"] = int(new_stock_quantity)
            with open("inventory.json", "w") as file:
             json.dump(inventory, file, indent=4)
            print("Stock updated successfully!\n")
            break
    else:
        print("Product ID not found.\n")

    options()

def option_4():
    print("Search Product")
    with open("inventory.json", "r") as file:
        inventory = json.load(file)

    product_id = input("Enter Product ID: ")
    for product in inventory:
        if product["ID"] == product_id:
            print("\nProduct Found")
            print("---------------------------------")
            print(f"ID: {product['ID']} | Name: {product['Name']} | Price: {product['Price']} | Stock: {product['Stock']}")
            print("---------------------------------\n")
            break
    else:
        print("Product ID not found.\n")

    options()

def option_5():
    print("Saving Inventory before exit...")
    with open("inventory.json", "r") as file:
        inventory = json.load(file)

    with open("inventory.json", "w") as file:
        json.dump(inventory, file, indent=4)

    print("Inventory saved successfully.\n")
    options()

def options():
    user_input = input("Enter Option: ")

    if user_input == "1":
        option_1()
    elif user_input == "2":
        option_2()
    elif user_input == "3":
        option_3()
    elif user_input == "4":
        option_4()
    elif user_input == "5":
        option_5()
    elif user_input == "6":
        print("Thank you for usingInventory Management System.\nProgram terminated.")

data_representation()
options()
