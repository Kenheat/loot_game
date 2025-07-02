from backpack import *
from game_actions import *

def main():
    start_message()

    bp = Backpack()
    valid_commands = ["E", "H", "i", "r", "l", "m"]

    while True:
        user_input = input("> ")

        if user_input not in valid_commands:
            print('\nInvalid command, type "H" for help menu.\n')

        if user_input == "E":
            print("\nGoodbye!\n")
            return
        
        if user_input == "H":
            help()
        
        if user_input == "i":
            bp.show_items_backpack()

        if user_input == "r":
            bp.remove_item()
        
        if user_input == "l":
            looted_items = loot()
            
            if looted_items:
                bp.loot_to_add(looted_items)
        
        if user_input == "m":
            bp.move_item()

if __name__ == "__main__":
    main()
