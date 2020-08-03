print('Hello user, Welcome to the age grouping app \n')

age= int(input('\n Please what is your age in numbers? '))

if age == 0 or age <= 12:
    print('Kid')
elif age<=30  or age <= 19:
    print('Teenager')
elif age<=20 or age<=30:
    print('Young Adult')
elif age<=31 or age<=64:
    print('Adult')
elif age>=65:
    print('Senior')
else:
    print('Please enter a number age.')