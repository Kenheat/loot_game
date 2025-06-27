from backpack import *
from game_actions import *

def main():
    print("Welcome to Loot Game!")
    print('Type "Exit" to exit game.')
    print('Type "Help" for help menu')

    bp = Backpack()

    while True:
        user_input = input("> ")

        if user_input == "Exit":
            return
        
        if user_input == "Help":
            help()
        
        if user_input == "I":
            bp.show_items()
        
        if user_input == "S":
            bp.show_available_backpack_space()

        # Not useful at this stage.
        #if user_input == "A":
            #item_to_add = input("Item to add: ")
            #bp.add_item(item_to_add)

        if user_input == "R":
            item_number = int(input("Item to remove: \n> "))
            bp.remove_item(item_number)
        
        if user_input == "L":
            looted_item = loot()
            print(f"Looted item: {looted_item}")
            keep_or_discard = input("Keep (K) or discard (D) item? \n> ")
            if keep_or_discard == "K":
                bp.add_item(looted_item)
                print("Item stored in backpack.")
            else:
                print("Item discarded.")

if __name__ == "__main__":
    main()
