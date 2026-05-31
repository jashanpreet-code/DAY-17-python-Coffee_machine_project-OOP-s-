from menu_items import menu_itemz, items
from coffee_maker import resourse
from money_machine import cash_system 


menus = items()
req = resourse()
cash = cash_system()
working = True
while working:
    print(f"{menus.get_items()}")
    order = input("WHICH COFFEE DO YOU WANT NAME IT := ")
    if order == "off":
        working = False
    elif order == "report":
        req.report()
    drink = menus.find_drink(order)
    if req.check_resources(drink) == True:
        print(f"you have to pay {cash.CURRENCY}{drink.cost}")
    if cash.payment_process(drink.cost) == False:
        working = False
    print("asf")
    req.coffe_maker(drink)
        
        
        
        
        
    
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

    