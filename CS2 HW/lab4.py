# lab 4
class Restaurant:
    def __init__(self):
        self.tables = {"1": 2, "2" : 4, "3" : 4, "4": 5}
        self.tables_reserved = {"1": False, "2" : False, "3" : False, "4": False}
        self.menu = {}
    
    def add_to_menu(self, key, value):
        self.menu[key] = value

    def print_menu(self):
        print("\nMenu:")
        for key in self.menu:
            print(f"{key} ${self.menu[key]}")

    def make_reservations(self):
        number_of_people = int(input("How large is your party?: "))
        booked = False
        for key in self.tables:
            if self.tables[key] >= number_of_people:
                self.tables_reserved[key] = True
                print(f"Table {key} is booked")
                booked = True
                break
        if not booked:
            print("We don't have a table to accomodate your party")

    
    def print_table_reservations(self):
        print(f"The tables available are:")
        for key in self.tables:
            if self.tables_reserved[key] == False:
                print(f"Table {key} has {self.tables[key]} seats")
    
    def build_menu(self):
        while True:
            item = input("Enter a menu item (enter done to finish):")
            if item.lower() == "done":
                print("Menu created succesfully!")
                break
            try:
                price = float(input(f"Enter the price for {item}: "))
                self.add_to_menu(item, price)
            except ValueError:
                print("That price is invalid")
    
    def take_order(self):
        menu_items_ordered = []
        price = 0.0
        order_more = "y"
        while order_more != "n":
            self.print_menu()
            order = input("Enter the name of the menu item you'd like to order: ")
            try:
                price += self.menu[order]
                menu_items_ordered.append([order, price])
            except:
                print("Item not found in menu")
            order_more = input("Do you want to order more?(enter n to complete order): ")
        if price > 0.0:
            print(f"Items ordered: {menu_items_ordered}")
            print(f"The total price for your order is ${price}")
        



