class Backpack():
    def __init__(self):
        self.empty = "(Empty)"
        self.items = {1: self.empty,
                      2: self.empty,
                      3: self.empty}
        self.max_backpack_space = len(self.items)
        self.available_backpack_space = len(self.items)
    
    def show_items(self):
        print("\nItems in backpack:\n")
        for item in self.items:
            print(" ---")
            print(f"| {item} | {self.items[item]}")
            print(" ---")
        print("")
    
    def show_available_backpack_space(self):
        print(f"Available backpack space: {self.available_backpack_space}")
    
    def remove_item(self):
        empty_count = 0
        for item in self.items:
            if self.items[item] is self.empty:
                empty_count += 1
        if empty_count == len(self.items):
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
        while True:
            item_to_move = int(input("\nChoose item to move (item number).\n> "))
            temp = self.items[item_to_move]
            if self.items[item_to_move] is not self.empty:
                destination = int(input(f"\nChoose where to move item {item_to_move} (slot number).\n> "))
                if self.items[destination] is self.empty:
                    self.items[destination] = self.items[item_to_move]
                    self.items[item_to_move] = self.empty
                    
                    print(f"\n{temp} moved from slot {item_to_move} to slot {destination}.\n")
                    return
                else:
                    print("\nItem already in selected slot.\n")
                    return
            else:
                print("\nNo item in selected slot.\n")
                return

    # TODO
    def replace_item(self):
        pass
    
    def add_item(self, looted_item):
        if self.available_backpack_space == 0:
            print("\nNo more available space in the backpack.\n")
            return
        for item in self.items:
            if self.items[item] is self.empty:
                self.items[item] = looted_item
                print(f"\n{looted_item} stored in backpack.\n")
                self.available_backpack_space -= 1
                return

    def loot_to_add(self, looted_items):
        # TODO: want the player to have the option of removing items from the backpack while looting
        while True:
            # problem(?): if the backpack is full, the option to loot is removed
            if self.available_backpack_space == 0:
                print("No more available space in the backpack.")
                return

            if len(looted_items) == 0:
                print("No more items in loot.\n")
                return

            # showing loot content
            print("\nLoot:\n") 
            for item in looted_items:
                print(" ---")
                print(f"| {item} | {looted_items[item]}")
                print(" ---")

            number_or_discard = input("\nChoose item to keep (item number) or discard all/rest of items (d).\n> ")

            if number_or_discard == "d":
                print("\nItems discarded.\n")
                return
            
            else:
                try:
                    number = int(number_or_discard)
                    popped_item = looted_items.pop(number)
                    self.add_item(popped_item) 
                    # problem if option of removing items from backpack while looting is implemented:
                    # if player tries to add item to a full bag, the item gets removed from loot (popped) either way
                    # and may end the loop since there's no more items in loot to deal with
                except:
                    print("Invalid choice.\n")
