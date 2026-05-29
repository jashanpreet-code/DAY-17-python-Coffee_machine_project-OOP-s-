from menu_items import coffes as cfm
from coffee_maker import resourse as rs


print("ENTER START TO MAKE COFFEE 'START':")
print("choice one of these coffes:")


ad = rs()
ad.report()

sd = cfm(milk = 30, sugar = 10, coffee =5, coffe_name = "latte",cost = 40)
sd.menus()
sd.get_items()

order = input("WHICH COFFEE DO YOU WANT NAME IT := ")


    