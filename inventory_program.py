# Inventory Tracker.
import sqlite3


def c_comm():
    connection.commit()
    connection.close()


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


# FIX ME!
def location_update():
    ("UPDATE inventory SET location = (?) WHERE item_id = (?)", (?, ?))

# FIX ME!
def delete_item():
    del_item_num = input("Enter Item Number To Add To Inventory: ")
    del_item_location = input("Enter Item Location Of Item Added To Inventory: ")
    verify_del_input = input(f"Are You Sure You Want To Add Item: {del_item_num} To Location: {del_item_location} Y/N: ")
    if verify_del_input == "Y" or "y":
        cursor.execute("DELETE FROM inventory WHERE ? = ?", (del_item_num, del_item_location))
        c_comm()
    else:
        pass



def add_item():
    add_item_num = input("Enter Item Number To Add To Inventory: ")
    add_item_location = input("Enter Item Location Of Item Added To Inventory: ")
    verify_input = input(f"Are You Sure You Want To Add Item: {add_item_num} To Location: {add_item_location} Y/N: ")
    if verify_input == "Y" or "y":
        cursor.execute("INSERT INTO inventory VALUES (?,?)", (add_item_num, add_item_location))
        c_comm()
    else:
        pass


# Create Database.
connection = sqlite3.connect('inventory_db')

# Define connection and cursor.
cursor = connection.cursor()

# Create inventory table command.
create_table = """CREATE TABLE IF NOT EXISTS
inventory (item_num INTEGER PRIMARY KEY, location TEXT)"""

# Create cursor and create inventory table.
cursor.execute(create_table)

user_choice()
c_comm()
