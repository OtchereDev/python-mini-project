import random

prompt="Choose Paper(p), Scissor(s), Paper(p), or Quit(q): "
Losses=0
Win=0
Draw=0
is_ended= False

while True:
    user_input=input(prompt)
    while user_input not in ['p','s','r','q']:
        print("Please enter the right option")
        user_input=print(input(prompt))
    if user_input == "q":
        break
    else:
        computer_choice=random.choice(["p","s","r"])
        if computer_choice=="p":
            move= "Paper"
        elif computer_choice=="s":
            move="Scissors"
        elif computer_choice=="r":
            move="Rock"
        print(f"Computer gave {move}")
        if computer_choice==user_input:
            Draw+=1
            print("Draw")
        elif (computer_choice=="r" and user_input=="p") or\
            (computer_choice=="p" and user_input=="s") or\
                (computer_choice=="s" and user_input=="r"):
                Win+=1
                print("You Won")
        else:
            print("You loss")
            Losses+=1
print(f"You have {Win} wins, {Losses} losses, and {Draw} draws")

    
    