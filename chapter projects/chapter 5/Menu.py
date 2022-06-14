# A simple menu program that the user can select an item from the menu to get a little details
# on the item selected


def main():
    # Initialize dictionary

    menu = {
        1: ["Black Desert", black_desert],
        2: ["Apex", apex],
        3: ["Starfield", starfield],
        4: ["Cyberpunk 2077", cyberpunk],
        5: ["Escape From Tarkov", escape_from_tarkov]
    }

    # call the print_list function to display the menu
    print_list(menu)

    # ask the user to enter their choice
    selection = input("please select a number from the list to learn more about that game. ")

    # call the invalid_selection function to check if the user entered a valid choice
    while invalid_selection(menu, selection):
        print("Invalid selection.\n")
        print_list(menu)
        selection = input("please select a number from the list to learn more about that game. ")

    selection = int(selection)
    print("\n" + menu[selection][0] + "\n" + menu[selection][1]())

# Function to print the menu
def print_list(menu):
    print("Game list")
    for key, value in menu.items():
        print(str(key) + ":", value[0])
    print("\n")

# Function to check if selection is valid
def invalid_selection(menu, selection):
    if selection.isdigit():
        selection = int(selection)

    if selection in menu:
        return False
    else:
        return True

# The following are functions that are used to return the description of each game to main to be displayed to the user.

def black_desert():
    return "An online MMORPG game that takes a lot of time investment to reach end game."
    
    
def apex():
    return "A battle royale game with futuristic elements."
    
    
def starfield():
     return "A RPG game from Bethesda coming in 2023."
    
    
def cyberpunk():
    return "A futuristic RPG game that had high expectations but lots of bugs at release."
    
    
def escape_from_tarkov():
    return "A survival looter shooter game with that keeps your adrenaline rushing."


main()
