import os

class Backpack():
    def __init__(self):
        self.empty = "(Empty)"
        self.items = {"1": self.empty,
                      "2": self.empty,
                      "3": self.empty}
        self.max_backpack_space = len(self.items)
        self.available_backpack_space = len(self.items)
    
    def show_items_backpack(self):
        os.system("clear")

        print("\nItems in backpack:\n")
        for item in self.items:
            print(" ---")
            print(f"| {item} | {self.items[item]}")
            print(" ---")
        print("")
    
    def remove_item(self):
        os.system("clear")
        self.show_items_backpack()

        if self.empty_count(self.items) == len(self.items):
            print("No items in backpack.\n")
            return
        
        item_number = input("\nItem to remove: \n> ")

        if item_number not in self.items:
            print("Invalid item number.\n")
            return

        if self.items[item_number] is self.empty:
            print("Selected slot is empty.\n")
            return

        temp_item = self.items[item_number]
        self.items[item_number] = self.empty
        self.show_items_backpack()
        print(f"{temp_item} removed from backpack.\n")
        self.available_backpack_space += 1
        
    def move_item(self):
        os.system("clear")
        self.show_items_backpack()

        # TODO add system for invalid commands
        while True:
            item_to_move = input("Choose item to move (item number).\n> ")
            temp_item = self.items[item_to_move]
            if self.items[item_to_move] is not self.empty:
                destination = input(f"Choose where to move item {item_to_move} (slot number).\n> ")
                if self.items[destination] is self.empty:
                    self.items[destination] = self.items[item_to_move]
                    self.items[item_to_move] = self.empty
                    
                    os.system("clear")
                    self.show_items_backpack()
                    print(f"{temp_item} moved from slot {item_to_move} to slot {destination}.\n")
                    return
                else:
                    print("\nItem already in selected slot.\n")
                    return
            else:
                print("\nNo item in selected slot.\n")
                return

    def replace_item(self, looted_items, item_to_replace, replacing_item):
        self.items[item_to_replace] = looted_items[replacing_item]
        looted_items[replacing_item] = self.empty
    
    def add_item(self, looted_item):
        for item in self.items:
            if self.items[item] is self.empty:
                self.items[item] = looted_item
                print(f"\n{looted_item} stored in backpack.\n")
                self.available_backpack_space -= 1
                return

    def show_items_loot(self, looted_items):
        print("\nLoot:\n")
        for item in looted_items:
            print(" ---")
            print(f"/ {item} / {looted_items[item]}")
            print(" ---")
        print("")

    def loot_to_add(self, looted_items):
        while True:
            while (self.available_backpack_space == 0) and (self.empty_count(looted_items) != len(looted_items)):
                os.system("clear")
                self.show_items_backpack()
                self.show_items_loot(looted_items)
                print("No more available space in the backpack.\n")
                
                # TODO add system for invalid commands
                replace_item = input("Replace item in backback with looted item?\ny/n> ")
                if replace_item == "y":
                    os.system("clear")
                    self.show_items_backpack()
                    self.show_items_loot(looted_items)
                    item_to_replace = input("Item to replace in backpack:\n> ")

                    replacing_item = input("Replacing item from loot:\n> ")

                    self.replace_item(looted_items, item_to_replace, replacing_item)
                    self.show_items_backpack()
                
                if self.empty_count(looted_items) == len(looted_items):
                    self.show_items_loot(looted_items)
                    print("No more items in loot.\n")
                    return

                if replace_item == "n":
                    print("\nLoot discarded.\n")
                    return

            os.system("clear")
            self.show_items_loot(looted_items)

            if self.empty_count(looted_items) == len(looted_items):
                print("No more items in loot.\n")
                return
            
            number_or_discard = input("Choose item to keep (item number) or discard all/rest of items (d).\n> ")

            if number_or_discard == "d":
                print("\nItems discarded.\n")
                return
            
            if number_or_discard not in looted_items:
                print("Invalid item number.")
            else:
                self.add_item(looted_items[number_or_discard])
                looted_items[number_or_discard] = self.empty
    
    def empty_count(self, items):
        count = 0
        for item in items:
            if items[item] is self.empty:
                count += 1
        return count
