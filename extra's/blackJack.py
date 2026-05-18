import random
import os

cards = [11,1,2,3,4,5,6,7,8,9,10,10,10,10]


def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def check(player_cards,computer_cards):
    if sum(computer_cards) == sum(player_cards):
        return "draw"
    elif sum(computer_cards) > sum(player_cards) and sum(computer_cards) < 21:
        return "computer wins"
    elif sum(player_cards) > sum(computer_cards) and sum(player_cards) < 21:
        return "player wins"
    elif sum(player_cards) > 21 and len(player_cards) == 3:
        return "computer wins"


def result(player_score,computer_score):
    print(type(computer_score),type(computer_score))
    if sum(computer_score) == sum(player_score):
        return "draw"
    elif sum(computer_score) > sum(player_score):
        return "computer wins"
    elif sum(player_score) > sum(computer_score):
        return "player wins"


def play_game():
        player_cards = []
        computer_cards = []
        computer_score = 0
        player_score = 0

        for _ in range(0,2):
            player_cards.append(random.choice(cards))
            computer_cards.append(random.choice(cards))
        print("the players card is =",player_cards)
        print("the computers first card is =",computer_cards)
        again = input("type 'y' for adding another card in player desk or type 'n' to pass ")
        if again == "y":
            player_cards.append(random.choice(cards))
            print("the players card is =",player_cards)
            print("the computers card is =",computer_cards)
            if 11 in player_cards and sum(player_cards) > 21:
                player_cards.remove(11)
                player_cards.append(1)
                print("the =",player_cards)
            print(check(player_cards, computer_cards),f"by computers cards is = '{computer_cards}' and the player cards is = '{player_cards}'")
            scorer = check(player_cards, computer_cards)
            if scorer == "computer wins":
                computer_score += 1
            else:
                 player_score += 1
            yes = input("Do you want to play again? (y/n)").lower()
            if yes == 'y' or not yes:
                clear()
                play_game()
            else:
                result(player_score,computer_score)
        else:
            print(check(player_cards, computer_cards),f"by computers cards is = '{computer_cards}' and the player cards is = '{player_cards}'")
            scorer = check(player_cards, computer_cards)
            if scorer == "computer wins":
                computer_score += 1
            else:
                player_score -= 1
            yes = input("Do you want to play again? (y/n)").lower()
            if yes == 'y' or not yes:
                play_game()
            else:
                result(player_score,computer_score)

play = input("Do you want to play the game then type 'y' if not submit 'n' = ")
if play.lower() == "y":
    clear()
    play_game()




# def computer():
#     computer_cards.append(random.choice(cards))
#     return computer_cards
#
# def player():
#     # print(computer()
#     player_cards.append(random.choice(cards))
#     return player_cards


# de.append(computer())


# def playAgain():
#     le = []

