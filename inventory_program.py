# Inventory Tracker.

# Database of locations will disappear after each program run but will create database later.
global inventory_dict
inventory_dict = {}

def user_choice():
    print("1: Find Location Of Item In Inventory")
    print("2: Change Item Location In Inventory")
    print("3: Delete Item From Inventory")
    print("4: Add Item To Inventory")

    # Get user input.
    user_input = int(input("Type Choice: "))

    # User input determines what happens.
    if user_input == 1:
        return find_location()
    if user_input == 2:
        return location_update()
    if user_input == 3:
        return delete_item()
    if user_input == 4:
        return add_item()
    else:
        return print("Not a choice, please try again.")


def find_location():
    return print("Find Location")


def location_update():
    return print("Update Location")


def delete_item():
    return print("Delete Item")


# FIX ME
def add_item():
    add_item_num = input("Enter Item Number To Add To Inventory: ")
    add_item_location = input("Enter Item Location Of Item Added To Inventory: ")
    verify_input = input("Are You Sure You Want To Add Item: {} To Location: {}. Y/N: ".format(add_item_num, add_item_location))
    if verify_input == "Y" or "y":
        inventory_dict.update({add_item_num: add_item_location})
    else:
        add_item()


user_choice()
