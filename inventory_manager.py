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
            
    else:
        with open("inventory.json", "w") as file:
            json.dump([], file)

def data_manipulation():
    
    pass

def data_persistence():
    pass

def build_menu_system():

    print("--------------MENU---------------")
    print("1. Display All Products")
    print("2. Add Product")
    print("3. Update Product")
    print("4. Search Product")
    print("5. Save Inventory")
    print("6. Exit")
    print("---------------------------------\n")

    user_input = input("Enter Option: ")

    if user_input == "1":
        print("Display All Products")
    elif user_input == "2":
        print("Add Product")
    elif user_input == "3":
        print("Update Product")
    elif user_input == "4":
        print("Search Product")
    elif user_input == "5":
        print("Save Inventory")
    elif user_input == "6":
        print("Exiting the program...")
        exit()

data_representation()
