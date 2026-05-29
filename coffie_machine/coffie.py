from data import resource as ra
from data import coffee as da
import sys


def which_coffee():
    while True:
        order = input("which coffee do you want (cappuccino,latte,espresso): ")
        if not order or order not in da.keys():
            input(f"please enter {da.keys()}")
            continue
        else:
            break
    return order



def payment_method(order):
    while True:
        cash = int(input(f"you have to pay ${da[order]['cost']} "))
        m = cash - da[order]['cost']
        if cash > da[order]['cost']:
            if m > ra['ingredients']['money']:
                print(f"i dont have enough money for your change = {m} please take your money back ${cash}")
                break
            print(f'this is your change ${m}')
            break
        elif cash < da[order]['cost']:
            print(f'your monet is not enough give me more ${m*-1}')
            continue
        else:
            return 1


def report():
    print(f'the ingredients quantity in machine is\n'
            f'milk = {ra['ingredients']['milk']}Mg\n'
            f'water = {ra['ingredients']['water']}Mg\n'
            f'coffee = {ra['ingredients']['coffee']}g\n')


def check_resources(order):
    if da[order]['ingredients']['water'] > ra['ingredients']['water']:
        return False
    elif da[order]['ingredients']['milk'] > ra['ingredients']['milk']:
        return False
    elif da[order]['ingredients']['coffee'] > ra['ingredients']['coffee']:
        return False


def make_coffee():
    while True:
        od = which_coffee()
        resource = check_resources(od)
        if resource == False:
            report()
            print("please refill the coffee machine")
            sys.exit()
        else:
            print(payment_method(od))
            ra['ingredients']['water'] -= da[od]['ingredients']['water']
            ra['ingredients']['milk'] -= da[od]['ingredients']['milk']
            ra['ingredients']['coffee'] -= da[od]['ingredients']['coffee']



make_coffee()























