# from menu_items import coffes as cf
class resourse:
    def __init__(self):
        self.res = {
            "milk" : 500,
            "coffe" : 200,
            "sugar" : 200,
        }
        
    def report(self):
        print("REPORT OF RESOURCES IN MACHINE:-")
        print(f"MILK = {self.res['milk']}")
        print(f"COFFEE = {self.res['coffe']}")
        print(f"SUGAR = {self.res['sugar']}")
    
    def check_resources(self,order):
        if self.res['milk'] - order.milk < 0:
            print(f"the milk is not sufficient fill milk in machine we only have {self.res['milk']}ML milk availble")
            return False
        elif self.res['sugar'] - order.sugar < 0:
            print(f"the sugar in not sufficient fill sugar in machine we only have {self.res['sugar']}Gm avilable")
            return False
        elif self.res['coffe'] - order.coffee < 0:
            print(f"the coffe is not sufficient to make a coffee fill some coffe in the machine we only have {self.res['coffee']}Mg avialable")
            return False
        else:
            return True
            
            
        
        