# Inventory Tracker.


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
