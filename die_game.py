import random

start_point = 0
end_point = 40
user_place= 0
computer_place= 0
computer_win= False
user_win = False
quit_game =False

while not user_win or not computer_win:
    user_input=input("Enter t to toss and play the game or enter q to quit: ")
    if user_input.lower() == "q":
        quit_game=True
        break
    if user_input.lower()=="t":
        user_move= random.randint(1,6)
        user_place+=user_move
        print(f"You moved for {user_move} steps")
        if user_place>end_point:
            overshoot= user_place-end_point
            user_place=end_point-overshoot
        print(f"You are at position {user_place} now\n")
        if user_place==end_point:
            user_win=True
            break


    computer_input=random.randint(1,6)
    computer_place+=computer_input
    print(f"The computer moved {computer_input} steps")
    if computer_place>end_point:
        overshoot=computer_place-end_point
        computer_place=end_point-overshoot
    print(f"Computer is at position {computer_place} steps\n")
    if computer_place==end_point:
            computer_win=True
            break

if quit_game:
    print(f"You are {end_point-user_place} steps to the end.")
elif user_win:
    print("You win")
elif computer_win:
    print("Computer win")

