
class cash_system:
    def __init__(self,dimes,pennies,nickles,quarters):
        self.dimes = 0.10
        self.pennies = 0.01
        self.nickles = 0.05
        self.quarters = 0.25
    
class money_control(cash_system):
    def __init__(self,recived_money,cost,profittes):
        self.recived_money = recived_money
        self.cost = cost
        self.profittes = profittes
        
    def proffite_report(self):
        print(f"Money: ${self.profittes}")
        
    def payment_check(self):
        pass
        
        