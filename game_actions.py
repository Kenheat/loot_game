from items import *

def help():
    print("Exit: exit game")
    print("I: show inventory")
    print("S: show available backpack space")
    print("A: add item to backpack")
    print("R: remove item from backpack")

def loot():
    item = Potion()
    return item