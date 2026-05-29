class menu:
    def __init__(self,milk,sugar,coffee,name,cost):
        self.name = name
        self.milk = milk
        self.sugar = sugar
        self.coffee = coffee
        self.cost = cost
        
        
class items:
    def __init__(self):
        self.menu = [
            menu(name = "latte" ,milk = 30, sugar = 10, coffee = 5, cost = 40),
            menu(name = "cappuccino" , milk = 30, sugar = 5, coffee = 5, cost = 50),
            menu(name = "lattee" , milk = 40, sugar = 10, coffee = 3, cost = 60)
        ]
     
        
    def get_items(self):
        print("MENU :-")
        for item in self.menu:
            print(item.name)
       
        
    def make_expresso(self):
     pass
 
