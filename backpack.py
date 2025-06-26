from items import *

class Backpack():
    def __init__(self):
        self.items = [Sword(), Sword(), Sword()]
        self.max_backpack_space = 5
        self.backpack_space = self.max_backpack_space - len(self.items)
    
    def show_items(self):
        print("Items:")
        print("---------")
        for item in self.items:
            print(item)
        print("---------")
    
    def show_backpack_space(self):
        return self.backpack_space
    
    def remove_item(self, item):
        if len(self.items) == 0:
            print("No items in backpack.")
            return
        self.items.remove(item)
        self.backpack_space += 1
    
    def add_item(self, item):
        if self.backpack_space == 0:
            print("No more space in the backpack.")
            return
        self.items.append(item)
        self.backpack_space -= 1
