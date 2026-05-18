# import data as d
# import random
#
# def one_question(question,user):
#     print(question)
#     if question[1].lower() == user.lower():
#         return True
#     else:
#         return False
#
#
# def pick_question():
#     question = random.choice(d.question_data)
#     return question['text'], question['answer']
#
# def check_answer(user_answer,correct_answer):
#     print(user_answer.lower())
#     print(correct_answer.lower())
#     if user_answer.lower() == correct_answer.lower():
#         return 1
#     else:
#         return 0
#
#
# while True:
#     text = pick_question()
#     print(f"QUESTION: {text[0]}")
#     user = input("enter your answer  in (True or False): ").lower()
#     if not user in ['true','false']:
#         print('Enter the correct answer only in the form of True Or False: ')
#     else:
#         is_correct = check_answer(user,text[1])
#         if is_correct == 1:
#             print("correct answer")
#         else:
#             print("wrong answer")
#         again = input("Do you want to play agin y or n: ").lower()
#         if again in ['y','n']:
#             continue
#         else:
#             break
#
#
#
#
#
# print(one_question(pick_question(),user))

################################### start OOPS ########################################
import random
import data as d
from Question_object import Question
from quiz_brain import quiz

quesiton_bank = []




















