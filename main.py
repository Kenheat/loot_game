from backpack import *
from help import *

def main():
    print("Welcome to Loot Game!")
    print('Type "Exit" to exit game.')
    print('Type "Help" for help menu')

    bp = Backpack()

    while True:
        text = input("> ")

        if text == "Exit":
            return
        
        if text == "Help":
            help()
        
        if text == "I":
            bp.show_items()
        
        if text == "S":
            print(f"Backpack space: {bp.show_backpack_space()}")

        if text == "A":
            item_to_add = input("Item to add: ")
            bp.add_item(item_to_add)

        if text == "R":
            item_to_remove = input("Item to remove: ")
            bp.remove_item(item_to_remove)

if __name__ == "__main__":
    main()
