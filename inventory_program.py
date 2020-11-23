# Inventory Tracker.
import sys
import sqlite3


def c_comm():
    """Commits an sqlite3 command and then closes the database."""
    connection.commit()
    connection.close()


def user_choice():
    """Choices for the user to do tasks with the sqlite3 database"""
    user_input = 0
    # Creates a while loop so that the user doesnt have to keep clicking on the program to run it.
    while user_input != 'N':
        print("1: Find Location Of Item In Inventory")
        print("2: Change Item Location In Inventory")
        print("3: Delete Item From Inventory")
        print("4: Add Item To Inventory")
        print("5: View Inventory")

        # The input that determines what the user wants to do from the print list above.
        user_input = input("Type Choice: ")

        # The text printed after each command.
        choose_string = "Choose A Number To Continue Or N To Exit: "

        # Stops the program if an n or N is encountered.
        if str(user_input).capitalize() == 'N':
            sys.exit()

        # Moves onto the find a location in the database function.
        if int(user_input) == 1:
            find_location()
            print(choose_string)

        # Moves onto location updating in the database function.
        if int(user_input) == 2:
            location_update()
            print(choose_string)

        # Moves onto the delete an item in the database function.
        if int(user_input) == 3:
            delete_item()
            print(choose_string)

        # Moves onto the add an item in the database function.
        if int(user_input) == 4:
            add_item()
            print(choose_string)

        # Moves onto the view database function.
        if int(user_input) == 5:
            view_inventory()
            print(choose_string)
        else:
            pass


def find_location():
    return print("FIX ME")


def location_update():
    return print("FIX ME")


def delete_item():
    del_item_num = input("Enter Item Number To Delete From Inventory: ")
    verify_del_input = input(f"Are You Sure You Want To Delete Item: {del_item_num} From The Inventory? Y/N: ")
    if verify_del_input == "Y" or "y":
        cursor.execute("DELETE FROM inventory WHERE item_num = (?)", del_item_num)
        c_comm()
    else:
        pass


def view_inventory():
    """Selects and returns everything from the sqlite3 database."""
    cursor.execute("SELECT * FROM inventory")
    results = cursor.fetchall()
    print(results)


def add_item():
    add_item_num = input("Enter Item Number To Add To Inventory: ")
    add_item_location = input("Enter Item Location Of Item Added To Inventory: ")
    verify_input = input(f"Are You Sure You Want To Add Item: {add_item_num} To Location: {add_item_location} Y/N: ")
    if verify_input == "Y" or "y":
        cursor.execute("INSERT INTO inventory VALUES (?,?)", (add_item_num, add_item_location))
        c_comm()
    else:
        pass


connection = sqlite3.connect('inventory_db')

# Define connection and cursor.
cursor = connection.cursor()

# Create inventory table command.
create_table = """CREATE TABLE IF NOT EXISTS
inventory (item_num INTEGER PRIMARY KEY, location TEXT)"""

# Create cursor and create inventory table.
cursor.execute(create_table)

user_choice()
