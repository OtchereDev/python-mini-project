import random

play_game= 'y'

while (play_game=='y'):
    answer= random.randint(1,50)
    try_number=int(input("Guess a number between 1 and 50: ")) 
    counter=1

    while try_number!=answer:
        if try_number>answer:
            print("Your guess is too large")
        if try_number<answer:
            print("Your guess is too small")
        try_number=int(input("Guess a number between 1 and 50: "))
        counter+=1
    print("You got it correct" +" "+ str(counter)+" "+"times")
    play_game=(input("Press y to continue:"))
     