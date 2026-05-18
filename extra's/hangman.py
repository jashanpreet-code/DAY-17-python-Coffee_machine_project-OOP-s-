import random

words = ["world","datab","error","visuals","python","hangman"]

def random_word():
      return random.choice(words)

levels = [r"""
              +-----+
              |     |
                    |
                    |
                    |
                    |
                    |
              ------+ ""","""       
              +-----+
              |     |
              0     |
                    |
                    |
                    |
                    |
              ------+ """, """
              +-----+
              |     |
              0     |
             /      |
                    |
                    |
                    |
              ------+ """, """
              +-----+
              |     |
              0     |
             /|     |
                    |
                    |
                    |
              ------+""","""
              +-----+
              |     |
              0     |
             /|\    |
                    |
                    |
                    |
              ------+""","""
              +-----+
              |     |
              0     |
             /|\    |
             /      |
                    |
                    |
              ------+""","""
              +-----+
              |     |
              0     |
             /|\    |
             / \    |
                    |
                    |
              ------+"""
              ]

# for i in levels:
#     print(i)
def display_word(word, geussed):
      display = ''
      for letter in word:
            if letter in geussed:
                  display += letter
            else:
                  display += '_'
      print(display)
      return display



def hangman(level, word):
      geussed = ''
      while level <= 7:
            while True:
                  guessing =  input("enter the character for guessing the word: ")
                  if guessing.isalpha() and len(guessing) == 1:
                        break
            checker = check_guess(word, guessing)
            print(word)
            if checker:
                  print("you guessed it right")
                  print(levels[level])
                  geussed += guessing
                  current_progess = display_word(word, geussed)
                  if current_progess == word:
                        print("you won the game")
                        break
            else:
                  print(levels[level])
                  level += 1
            if level == 7:
                  print("you lost the game")
            # for i in range(len(random_word())):
            #       if guessing in str(i):
            #             print(i)
      
      
def check_guess(word, guessing):
      print(guessing in word)
      return guessing in word

hangman(0,random_word())












