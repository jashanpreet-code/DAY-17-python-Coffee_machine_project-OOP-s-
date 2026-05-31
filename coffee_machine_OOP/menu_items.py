class menu_itemz:
    def __init__(self,milk,sugar,coffee,name,cost):
        self.name = name
        self.milk = milk
        self.sugar = sugar
        self.coffee = coffee
        self.cost = cost
        
        
class items:
    def __init__(self):
        self.menu = [
            menu_itemz(name = "latte" ,milk = 30, sugar = 10, coffee = 5, cost = 7),
            menu_itemz(name = "cappuccino" , milk = 30, sugar = 5, coffee = 5, cost = 6),
            menu_itemz(name = "expresso" , milk = 40, sugar = 10, coffee = 3, cost = 5)
        ]
     
     
        
    def get_items(self):
        print("MENU :-")
        options = ""
        for item in self.menu:
            options += f"{item.name} \t"
        return options
       
        
    def find_drink(self,order):
        for item in self.menu:
            if order == item.name:
                return item
        print("we don't have this drink")
        return None
 
