import os

class Backpack():
    def __init__(self):
        self.empty = "(Empty)"
        self.items = {1: self.empty,
                      2: self.empty,
                      3: self.empty}
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
    
    def show_available_backpack_space(self):
        print(f"Available backpack space: {self.available_backpack_space}")
    
    def remove_item(self):
        os.system("clear")

        if self.empty_count(self.items) == len(self.items):
            print("\nNo items in backpack.\n")
            return
        
        try:
            item_number = int(input("\nItem to remove: \n> "))
            if self.items[item_number] is self.empty:
                print("\nSelected slot is empty.\n")
                return

            print(f"\n{self.items[item_number]} removed from backpack.\n")
            self.items[item_number] = self.empty
            self.available_backpack_space += 1
        except:
            print("\nInvalid choice.\n")
    
    def move_item(self):
        os.system("clear")
        self.show_items_backpack()

        while True:
            item_to_move = int(input("\nChoose item to move (item number).\n> "))
            temp = self.items[item_to_move]
            if self.items[item_to_move] is not self.empty:
                destination = int(input(f"\nChoose where to move item {item_to_move} (slot number).\n> "))
                if self.items[destination] is self.empty:
                    self.items[destination] = self.items[item_to_move]
                    self.items[item_to_move] = self.empty
                    
                    os.system("clear")
                    print(f"\n{temp} moved from slot {item_to_move} to slot {destination}.\n")
                    self.show_items_backpack()
                    return
                else:
                    print("\nItem already in selected slot.\n")
                    return
            else:
                print("\nNo item in selected slot.\n")
                return

    # TODO refine
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
            if (self.available_backpack_space == 0) and (self.empty_count(looted_items) != len(looted_items)):
                print("No more available space in the backpack.")
                
                # TODO refine
                replace_item = input("Replace item in backback with looted item?\ny/n> ")
                if replace_item == "y":
                    os.system("clear")
                    self.show_items_backpack()
                    item_to_replace = int(input("Item to replace:\n> "))

                    os.system("clear")
                    self.show_items_loot(looted_items)
                    replacing_item = int(input("Item to replace with:\n> "))

                    self.replace_item(looted_items, item_to_replace, replacing_item)

                if replace_item == "n":
                    print("Loot discarded.")
                    return

            if self.empty_count(looted_items) == len(looted_items):
                print("No more items in loot.\n")
                return

            # TODO make system for clearing console at e right time
            os.system("clear")
            self.show_items_loot(looted_items)

            number_or_discard = input("\nChoose item to keep (item number) or discard all/rest of items (d).\n> ")

            if number_or_discard == "d":
                print("\nItems discarded.\n")
                return
            
            else:
                try:
                    number = int(number_or_discard)
                    self.add_item(looted_items[number])
                    looted_items[number] = self.empty
                except:
                    print("Invalid choice.\n")
    
    def empty_count(self, items):
        count = 0
        for item in items:
            if items[item] is self.empty:
                count += 1
        return count
