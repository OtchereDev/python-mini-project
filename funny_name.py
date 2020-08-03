import sys, random

print("\n This is the random name generaor that allow you to load an undercover name")
print("\n\n Help yourself and dont be caught\n")

firstName=('Baby Oil','Bad News','Big Burps',"Bill 'Beenie­Weenie'","Bob 'Stinkbug'",'Bowel Noises',
            'Boxelder',"Bud 'Lite' ",'Butterbean','Buttermilk','Buttocks','Chad','Chesterfield',
            'Chewy','Chigger","Cinnabuns','Cleet','Cornbread','Crab Meat','Crapps','Dark Skies','Dennis Clawhammer',
            'Dicman','Elphonso','Fancypants','Figgs','Foncy','Gootsy','Greasy Jim','Huckleberry',
            'Snorki','Soupcan Sam','Spitzitout','Squids','Stinky','Storyboard','Sweet Tea','TeeTee','Wheezy Joe')

lastName=('Appleyard','Bigmeat','Bloominshine','Boogerbottom',\
          'Breedslovetrout','Butterbaugh','Clovenhoof','Clutterbuck',\
          'Cocktoasten','Endicott','Fewhairs','Gooberdapple','Goodensmith',\
          'Goodpasture','Guster','Henderson','Hooperbag','Hoosenater',\
          'Hootkins','Jefferson','Jenkins','Jingley­Schmidt','Johnson',\
          'Kingfish','Listenbee',"M'Bembo",'McFadden','Moonshine','Nettles')

while True:
    first=random.choice(firstName)
    last = random.choice(lastName)
    print("Your Undercover name is : \n")
    print ("{}{}".format(first,last), file=sys.stderr)

    print("\n\n")
    print("\n Play Again? \n")
    print("Press Enter to continue, or n to Quit \n\n")

    userAnswer=input("Would you like to continue for a more suitable name: \n")
    if userAnswer.lower()=="n":
        break

input("\n Press Enter to exit the program.")
