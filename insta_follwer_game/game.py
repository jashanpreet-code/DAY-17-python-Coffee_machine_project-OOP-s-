import data as da
import random



def main():
    first = random.choice(da.info)
    second = random.choice(da.info)
    print(f"the name is {first['name']} and profession if {first['profession']} and residence of {first['country']}")
    print("In comparison with :-")
    print(f"The name is {second['name']} and  profession is {second['profession']} and residence of {second['country']}")
    compare = input("enter 'l' of the frist person followers are less then second person if not then type 'h' (l/h) ")
    if compare == 'l':
        if first['followers'] < second['followers']:
            print("you are wright")
            restart()
        else:
            print("you are wrong")
            restart()
    else:
        if first['followers'] < second['followers']:
            print("you are wright")
            restart()
        else:
            print("you are wrong")
            restart()

def restart():
    rs = input("press 'y' to restart or enter to continue and  'n' for stop playing ").lower()
    if rs == 'y' or not rs:
        main()

main()