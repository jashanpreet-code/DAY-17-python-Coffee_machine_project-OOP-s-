from menu_items import menu as cfm, items as it
from coffee_maker import resourse as rs
from money_machine import money_control as mc 



starter = input("ENTER START TO MAKE COFFEE 'START':")
reports = input("IF YOU WANT THE RESOURSE REPORT JUST WRITE 'resourse' AND IF YOU WANT MONEY REPORT ENTER 'money':=")
if reports == "money":
    mc.proffite_report
elif reports == "resourse":
    rs.report
else:
    pass
print("choice one of these coffes:")


# ad = rs()
# ad.report()

# sd = cfm(milk = 30, sugar = 10, coffee =5, coffe_name = "latte",cost = 40)
it.get_items()

order = input("WHICH COFFEE DO YOU WANT NAME IT := ")
rs.check_resources(order)

    