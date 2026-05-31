
class cash_system:
    CURRENCY = '$'
    COINS = {
        "dimes" : 0.10,
        "pennies" : 0.01,
        "nickles" : 0.05,
        "quarters" : 0.25
    }
      
    def __init__(self):
        self.money_recived = 0
        self.profit = 0

        
    def proffite_report(self):
        print(f"Money: ${self.profit}")
        
    def payment_check(self):
        print("INSERT COINS:=")
        for i in self.COINS:
            self.money_recived += int(input(f"how many {i} ")) * self.COINS[i]  
        return self.money_recived          
        
        
    def payment_process(self,cost):
        self.payment_check()
        if self.money_recived > cost:
            change = round(self.money_recived - cost,2)
            print(f"here is your change {self.CURRENCY}{change}")
            self.profit += cost
            self.money_recived = 0
        else:
            print("your money is not enough")
            self.money_recived = 0
            return False
            
            