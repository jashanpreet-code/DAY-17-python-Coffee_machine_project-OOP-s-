class resourse:
    def __init__(self):
        self.res = {
            "milk" : 500,
            "coffe" : 200,
            "shugar" : 200,
        }
        
        
    def report(self):
        print("REPORT OF RESOURCES IN MACHINE:-")
        print(f"MILK = {self.res['milk']}")
        print(f"COFFEE = {self.res['coffe']}")
        print(f"SHUGAR = {self.res['shugar']}")
    