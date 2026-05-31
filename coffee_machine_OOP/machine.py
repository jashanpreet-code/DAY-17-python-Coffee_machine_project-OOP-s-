from menu_items import menu_itemz, items
from coffee_maker import resourse
from money_machine import cash_system 


menus = items()
req = resourse()
cash = cash_system()
working = True
while working:
    starter = input("ENTER START TO MAKE COFFEE 'START':").lower()
    reports = input("IF YOU WANT THE RESOURSE REPORT JUST WRITE 'resourse' AND IF YOU WANT MONEY REPORT ENTER 'money':=").lower()
    print(f"{menus.get_items()}")
    order = input("WHICH COFFEE DO YOU WANT NAME IT := ")
    if order == "off":
        working = False
    elif order == "report":
        req.report()
    drink = menus.find_drink(order)
    if req.check_resources(drink) == True:
        print(f"you have to pay {drink.cost}")
        ad = drink.cost
        cash.payment_check(ad)
        
        
        
        
        
    
    # if reports == "money":
    #     mc.proffite_report
    # elif reports == "resourse":
    #     rs.report
    # else:
    #     print("CHOICE ONE OF THESE COFFES:")
    #     it.get_items


# ad = rs()
# ad.report()

# sd = cfm(milk = 30, sugar = 10, coffee =5, coffe_name = "latte",cost = 40)
# it.get_items()

# rs.check_resources(order)

    