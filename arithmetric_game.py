import random
import time


class ArithmetricGame():
    def __init__(self,ques_num):
        self.ques_num =ques_num
    def generate_question(self):
        operand_1 = random.randint(1,100)
        operand_2 = random.randint(1,100)
        operator = random.choice(["+","-","*","/"])
        if operator == "+":
            answer= operand_1 + operand_2
        if operator == "-":
            answer = operand_1 - operand_2
        if operator == "*":
            answer = operand_1 * operand_2
        if operator == "/":
            answer = operand_1 / operand_2
        question = str(operand_1) + " " + operator + " "+ str(operand_2)+" :"
        return question,answer

    def play_game(self):
        num_correct=0
        start_time= time.time()
        for i in range(self.ques_num):
            print("Question "+ str(i+1)+" :")
            question,answer= self.generate_question()
            print(question)
            user_answer = int(input("What is your answer: "))
            if user_answer == answer:
                num_correct += 1
                print("You got the answer correct")
            else:
                print("You got the question wrong. The correct answer is "+ str(answer))
        end_time=time.time()
        print("you got "+ str(num_correct)+" questions correct")
        print("you use {0:.3f}s to answer the question".format(end_time-start_time))



new_game=ArithmetricGame(10)
new_game.play_game()