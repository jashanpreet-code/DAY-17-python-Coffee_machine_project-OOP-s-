class quiz:
    def __init__(self,q_list):
        self.score = 0
        self.q_list = q_list
        self.question_number = 0

    def more_question(self):
        if self.question_number < len(self.q_list):
            print(f"your current score is {self.score} / {self.question_number}")
            return True
        play = input("if you to play agin 'y' if not 'n' or 'Press Enter' " )
        if play.lower() == 'y':
            self.question_number = 0
            self.score = 0
            return True
        else:
            print("thank you for playing")
            return False
    
    def next_question(self):
        current_question = self.q_list[self.question_number]
        self.question_number += 1
        user_answer = input(f"{self.question_number} {current_question.text} (True/False): ")
        self.check_answer(user_answer,current_question.answer)

    def check_answer(self,user_answer,current_answer):
        if user_answer.lower() == current_answer.lower():
            self.score += 1
            print(" ✅ Correct")
        else:
            print("❌ Wrong")
            print(f"score: {self.score}/{self.question_number}")
            print(f"correct answer: {current_answer}")

