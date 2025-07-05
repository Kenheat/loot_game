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
    
    def show_items_loot(self, looted_items):
        print("\nLoot:\n")
        for item in looted_items:
            print(" ---")
            print(f"/ {item} / {looted_items[item]}")
            print(" ---")
        print("")
    
    def remove_item(self):
        self.show_items_backpack()

        if self.empty_count(self.items) == len(self.items):
            print("No items in backpack.\n")
            return
        
        while True:
            user_input = input('Choose item to remove (item number).\nType "a" to abort.\n> ')

            if self.abort_action(user_input, "\nRemoval of item aborted.\n"):
                return

            if self.invalid_command(user_input, self.items, "\nInvalid item number.\n"):
                continue

            if self.items[user_input] is self.empty:
                print("\nSelected slot is empty.\n")
                continue

            temp_item = self.items[user_input]
            self.items[user_input] = self.empty
            self.show_items_backpack()
            print(f"{temp_item} removed from backpack.\n")
            self.available_backpack_space += 1
            
            return
    
    def move_item(self):
        self.show_items_backpack()

        while True:
            item_to_move = input('Choose item to move (item number).\nType "a" to abort.\n> ')

            if self.abort_action(item_to_move, "\nMoving of item aborted.\n"):
                return

            if self.invalid_command(item_to_move, self.items, "\nInvalid item number.\n"):
                continue

            if self.items[item_to_move] is self.empty:
                print("\nNo item in selected slot.\n")
                continue

            while self.items[item_to_move] is not self.empty:
                destination = input(f'\nChoose where to move item {item_to_move} (slot number).\nType "a" to abort.\n> ')

                if self.abort_action(destination, "\nMoving of item aborted.\n"):
                    return
                
                if self.invalid_command(destination, self.items, "\nInvalid slot number."):
                    continue
                    
                if self.items[item_to_move] == self.items[destination]:
                    print("\nCan't move item to same slot")
                    continue

                if self.items[destination] is self.empty:
                    temp_item = self.items[item_to_move]
                    self.items[destination] = self.items[item_to_move]
                    self.items[item_to_move] = self.empty
                    
                    self.show_items_backpack()
                    print(f"{temp_item} moved from slot {item_to_move} to slot {destination}.\n")
                    return
                
                temp_item_to_move = self.items[item_to_move]
                temp_item_destination = self.items[destination]

                self.items[destination] = self.items[item_to_move]
                self.items[item_to_move] = temp_item_destination
                self.show_items_backpack()
                print(f"{temp_item_to_move} switched with {temp_item_destination}.\n")
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

    def loot_to_add(self, looted_items):
        self.show_all_inventory(looted_items)

        while True:

            while (self.available_backpack_space == 0) and (self.empty_count(looted_items) != len(looted_items)):
                self.show_all_inventory(looted_items)
                
                print("No more available space in the backpack.\n")
                
                while True:
                    replace_item = input("Replace item in backback with looted item?\ny/n> ")

                    if self.invalid_command(replace_item, ["y", "n"], "\nInvalid command.\n"):
                        continue

                    if replace_item == "n":
                        print("\nLoot discarded.\n")
                        return

                    if replace_item == "y":
                        self.show_all_inventory(looted_items)
                        
                        while True:
                            item_to_replace = input('Item to replace in backpack:\nType "a" to abort.\n> ')
                            if self.abort_action(item_to_replace, ""): # error message gets cleared immediately
                                break
                            if self.invalid_command(item_to_replace, self.items, "\nInvalid command.\n"):
                                continue

                            replacing_item = input('\nReplacing item from loot:\nType "a" to abort.\n> ')
                            if self.abort_action(replacing_item, ""): # error message gets cleared immediately
                                break
                            if self.invalid_command(replacing_item, looted_items, "\nInvalid command.\n"):
                                continue
                            if looted_items[replacing_item] is self.empty:
                                print("\nCan't replace item with empty slot.\n")
                                continue

                            self.replace_item(looted_items, item_to_replace, replacing_item)

                            break
                    
                    break

            if self.empty_count(looted_items) == len(looted_items):
                self.show_all_inventory(looted_items)
                print("No more items in loot.\n")
                return
            
            number_or_discard = input("Choose item to keep (item number) or discard all/rest of items (d).\n> ")

            if number_or_discard == "d":
                print("\nItems discarded.\n")
                return
            
            if self.invalid_command(number_or_discard, looted_items, "\nInvalid item number.\n"):
                continue

            self.add_item(looted_items[number_or_discard])
            looted_items[number_or_discard] = self.empty

            self.show_all_inventory(looted_items)
    
    def empty_count(self, items):
        count = 0
        for item in items:
            if items[item] is self.empty:
                count += 1
        return count

    def invalid_command(self, item_to_check, what_to_check, error_message):
        if item_to_check not in what_to_check:
            print(error_message)
            return True
        
    def show_all_inventory(self, looted_items):
        self.show_items_backpack()
        self.show_items_loot(looted_items)

    def abort_action(self, user_input, abort_message):
        if user_input == "a":
            print(abort_message)
            return True
