# Inventory Tracker.
# Inventory tracker, database will be a text file, security
# concerns for text file, public inventory list instead of private.
# Can also create an ini file for dictionary saving but I don't know how to do that yet so using text files for now.

# import pickle


# Load the dictionary back from the pickle file.
# favorite_color = pickle.load( open( "save.p", "rb" ) )


# The inventory stored as a dictionary.
inventory_dict = {}
inventory_dict.update({'item3': 3})


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


def add_item():
    return print("Add Item")


user_choice()

# Save a dictionary into a pickle file.
# favorite_color = { "lion": "yellow", "kitty": "red" }
# pickle.dump( favorite_color, open( "save.p", "wb" ) )
