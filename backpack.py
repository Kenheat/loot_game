from items import *

class Backpack():
    def __init__(self):
        self.items = [Sword(), Sword(), Sword(), Sword(), Sword()]
        self.max_backpack_space = 5
        self.available_backpack_space = self.max_backpack_space - len(self.items)
    
    def show_items(self):
        print("Items:")
        print("---------")
        item_index = 1
        for item in self.items:
            print(f"{item_index}. {item}")
            item_index += 1
        print("---------")
    
    def show_available_backpack_space(self):
        print(f"Available backpack space: {self.available_backpack_space}")
    
    def remove_item(self, item_number):
        if len(self.items) == 0:
            print("No items in backpack.")
            return
        del self.items[item_number - 1]
        self.available_backpack_space += 1
    
    def add_item(self, item):
        if self.available_backpack_space == 0:
            print("No more available space in the backpack.")
            return
        self.items.append(item)
        self.available_backpack_space -= 1
