class Backpack():
    def __init__(self):
        self.empty = "(Empty)"
        self.items = {1: self.empty,
                      2: self.empty,
                      3: self.empty,
                      4: self.empty,
                      5: self.empty}
        self.max_backpack_space = len(self.items)
        self.available_backpack_space = len(self.items)
    
    def show_items(self):
        print("Items in backpack:\n")
        for item in self.items:
            print(" ---")
            print(f"| {item} | {self.items[item]}")
            print(" ---")
    
    def show_available_backpack_space(self):
        print(f"Available backpack space: {self.available_backpack_space}")
    
    def remove_item(self, item_number):
        if len(self.items) == 0:
            print("No items in backpack.")
            return
        print(f"{self.items[item_number]} removed from backpack.")
        self.items[item_number] = self.empty
        self.available_backpack_space += 1
    
    def add_item(self, looted_item):
        if self.available_backpack_space == 0:
            print("No more available space in the backpack.")
            return
        for item in self.items:
            if self.items[item] is self.empty:
                self.items[item] = looted_item
                print("Item stored in backpack.")
                self.available_backpack_space -= 1
                return
