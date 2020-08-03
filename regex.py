import re

#this is a regex for website verifier with http:// or https://
# web_reg= re.compile(r'^[http://]|^[https://]')

# web_input= input("Enter your web address: \n\t")

# if web_reg.search(web_input) != None:
#     print('This website has http or https')
# else:
#     print('It doesnt')


#this is the date finder 
# date_reg = re.compile(r'''
#     (^(\d|\d{2}|\d{4})
#     (\s|-|/|,|\.)
#     (\d{1}|\d{2})
#     (\s|-|/|,|\.)
#     (\d|\d{2}|\d{4})$)
# ''',re.VERBOSE)

# date_check = input("let check the date: \n\t")

# if date_reg.search(date_check) != None:
#     print('You go it that a date')
# else:
#     print('Nope that isnt a date')

#this does the formating with .sub()
# date_replace=re.compile(r'(\s|-|/|,)')

# mo =date_replace.sub('-','20/8/2020')

# print(mo)

# formats date with for loop and .join
# formatted_date= []
# for groups in date_reg.findall(date_check):
#     new_format='-'.join([groups[1],groups[3],groups[5]])
#     formatted_date.append(new_format)

# print(formatted_date)

#search a neatly formatted number d,ddd,ddd etc
# search=re.compile(r'^\d{1,3}(,\d{3})*$')

# n=input("Enter the number\n\t")

# if search.search(n) != None:
#     print('You go it that a number')
# else:
#     print('Nope that isnt a number')

#search for name with Nakamoto as surname
# name=re.compile(r'[A-Z][a-z]+\sNakamoto$')

# en=input('please enter your name:\n\t')

# print(name.search(en))

#check for sentence
# check = re.compile(r'(Alice|Bob|Carol)\s(eats|pets|throws)\s(apples|cats|baseballs)\.', re.IGNORECASE)
# search=input("enter the sentence\n\t")
#print(check.search(search))

#check for strong password
# def strong_password(n):
#     password = re.compile(r'[A-Za-z0-9]+\.?[@!%$]')
#     if len(n) < 8:
#         print('Your password is weak, it should have a length greater than 8')
#     if password.search(n) != None:
#         print("Great password")
#     if password.search(n) == None:
#         print("Your password combo is bad. Try Again!")

# check=input("Create a password\n\t")
# strong_password(check)


#regex version of strip()
string= input("Enter a string to strip:\n\t")
bad_char=(input("Enter the character you want to be stripped") or "")


def regex_strip(string,bad_char):
    strip_regex=re.compile(r'[%s]' %bad_char)
    return strip_regex.sub('',string)

print(regex_strip(string,bad_char))