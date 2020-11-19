# Inventory Tracker.
# Inventory tracker, database will be a text file, security concerns for text file, public inventory list instead of private.
# Can also create an ini file for dictonary saving but I dont know how to do that yet so using text files for now.

# import pickle
# Save a dictionary into a pickle file.
# favorite_color = { "lion": "yellow", "kitty": "red" }
# pickle.dump( favorite_color, open( "save.p", "wb" ) )

#
# Load the dictionary back from the pickle file.
# favorite_color = pickle.load( open( "save.p", "rb" ) )



# The inventory stored as a dictionary.
inventory_dict = {}
def user_choice(user_input=int(input("Type Choice: "))):
    if user_input == 1:
        return print(1)
    if user_input == 2:
        return print(2)
    if user_input == 3:
        return print(3)
    if user_input == 4:
        return print(4)
    else:
        return print("Not a choice, please try again.")


# Get user input.
print("1: Find Location Of Item")
print("2: Change Item Location")
print("3: Delete Item")
print("4: Add Item To Outgoing")

user_choice()
