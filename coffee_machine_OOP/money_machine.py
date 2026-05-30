
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
        
        
        