class coffes:
    def __init__(self,milk,sugar,coffee,coffe_name,cost):
        self.milk = milk
        self.sugar = sugar
        self.coffee = coffee
        self.coffe_name = coffe_name
        self.cost = cost
        self.menu = {}
        
    def menus(self):
        self.menu = [
            "latte" : {"milk" : 30, "sugar" : 10, "coffee" : 5, "cost" : 40},
            "cappuccino" : {"milk" : 30, "sugar" : 5, "coffee" : 5, "cost" :50},
            "lattee" : {"milk" : 40, "sugar" : 10, "coffee" : 3, "cost" : 60}
        ]
     
        
    def get_items(self):
        print("MENU :-")
        for item in self.menu:
            print(item)
       
        
    def make_expresso(self):
     pass
 
