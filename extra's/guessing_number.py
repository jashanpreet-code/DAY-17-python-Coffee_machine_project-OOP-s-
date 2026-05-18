import random
import os

def clean():
    os.system('cls' if os.name =='nt' else 'clear')

def agin_number():
    play()

def asign_number():
    return random.randint(1,100)

def check(guess, number):
    if guess == number:
        return 1
    elif guess < number:
        return -1
    elif guess > number:
        return 0

def game(turms, number):
    correct = False
    while turms > 0 and correct == False:
        guess = int(input("enter your guess: "))
        turms -= 1
        val = check(guess,number)
        if val == 0:
            print("too high")
            print(f"you have attempts = {turms}")
            if turms == 0:
             print("you are out of moves")
             ask()
        elif val == -1:
            print("too low")
            print(f"you have attempts = {turms}")
            if turms == 0:
              print("you are out of moves")
              ask()
        else:
            print("correct")
            print(f"attempts you have  = {turms}")
            if turms == 0:
                print("you are out of moves")
            correct = True
            ask()

def play():
    input("if you want to play again, press enter: ")
    level = input("enter which level to play easy or hard or press enter for normal play: ")
    number = asign_number()
    if level == "easy":
        turms = 15
        game(turms,number)
    elif level == "hard":
        turms = 5
        game(turms,number)
    else:
        turms = 10
        game(turms,number)

def ask():
    ch = input("do you want to play again ? (y/n)").lower()
    if ch == "y" or not ch:
        play()

play()