# A simple menu program that the user can select an item from the menu to get a little details
# on the item selected


def main():
    # Initialize dictionary

    menu = {
        1: ["Black Desert", "An online MMORPG game that takes a lot of time investment to reach end game."],
        2: ["Apex", "A battle royale game with futuristic elements."],
        3: ["Starfield", "A RPG game from Bethesda coming in 2023."],
        4: ["Cyberpunk 2077", "A futuristic RPG game that had high expectations but lots of bugs at release."],
        5: ["Escape From Tarkov", "A survival looter shooter game with that keeps your adrenaline rushing."]
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
    print("\n" + menu[selection][0] + "\n" + menu[selection][1])


def print_list(menu):
    print("Game list")
    for key, value in menu.items():
        print(str(key) + ":", value[0])
    print("\n")


def invalid_selection(menu, selection):

    if selection.isdigit():
        selection = int(selection)

    if selection in menu:
        return False
    else:
        return True


main()
