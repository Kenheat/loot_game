class Backpack():
    def __init__(self):
        self.items = []
        self.max_backpack_space = 5
        self.available_backpack_space = self.max_backpack_space - len(self.items)
    
    def show_items(self):
        print("Items in backpack:\n")
        item_index = 1
        for i in range(5):
            print(" ---")
            try:
                print(f"| {item_index} | {self.items[i]}")
                print(" ---")
            except:
                print(f"| {item_index} | (Empty)")
                print(" ---")
            item_index += 1
    
    def show_available_backpack_space(self):
        print(f"Available backpack space: {self.available_backpack_space}")
    
    def remove_item(self, item_number):
        if len(self.items) == 0:
            print("No items in backpack.")
            return
        print(f"{self.items[item_number - 1]} removed from backpack.")
        del self.items[item_number - 1]
        self.available_backpack_space += 1
    
    def add_item(self, item):
        if self.available_backpack_space == 0:
            print("No more available space in the backpack.")
            return
        self.items.append(item)
        print("Item stored in backpack.")
        self.available_backpack_space -= 1
