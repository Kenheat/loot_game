from items import Sword, Potion, Chestpiece
import random

def start_message():
    print("")
    print("Welcome to Loot Game!")
    print("")
    print('Type "E" to exit game.')
    print('Type "H" for help menu.')
    print("")

def help():
    print("")
    print("E: exit game")
    print("i: show inventory")
    print("s: show available backpack space")
    print("l: loot item")
    print("   <item number>: add chosen item to backpack")
    print("   d: discard looted item")
    print("r: remove item from backpack")
    print("")

def loot():
    items = [Sword(), Potion(), Chestpiece()]
    looted_items = {}

    # randomizing number of items and items in loot
    random_range_number = random.randrange(4)
    for i in range(random_range_number):
        looted_items[i + 1] = (items[random.randrange(len(items))])

    if len(looted_items) == 0:
        print("\nNo loot, try again!\n")
        return None
    
    return looted_items
