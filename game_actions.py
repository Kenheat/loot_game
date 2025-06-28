from items import Sword, Potion, Chestpiece
import random

def help():
    print("Exit: exit game")
    print("I: show inventory")
    print("S: show available backpack space")
    print("L: loot item")
    print("   K: keep looted item")
    print("   D: discard looted item")
    print("R: remove item from backpack")

def loot():
    items = [Sword(), Potion(), Chestpiece()]
    looted_item = items[random.randrange(len(items))]
    print(f"Looted item: {looted_item}")
    return looted_item
