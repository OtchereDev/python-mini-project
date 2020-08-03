def main():
    while True:
        user_word=[]
        take = input("Enter enter a word that you want a pig latin of :\n\n")
        user_word.append(take)
        vowels =["a","e","i","o","u"]

        if user_word[0][0] in vowels:
            latin = user_word[0]+"way"
            print(latin)

        else:
            latin= user_word[0]+"ay"
            print(latin)

        print("\n\n Would you like to generate new pig latin")
        user_break=input("Enter p to quit but press enter to continue")

        if user_break.lower() == "p":
            break


if __name__ == "__main__":
    main()