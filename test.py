# for i in range(0, 3):
#     for j in range(0, 3):
#         continue
#     print(i+j)


# Employees =[["John Mckee", 38, "Sales"],["Lisa Crawford",29,"Marketing"],["Sujan Patel",28,"HR"]]

# for Employee in Employees:
    
#     print("Name: ", Employee[0])
#     print("Age: ", Employee[1])
#     print("Department: ", Employee[2])
#     print('-'*20)

# X = [[1,2,3],[4,5,6],[7,8,9]] 
# Y = [[10,11,12],[13,14,15],[16,17,18]] 
# result = [[0,0,0],[0,0,0],[0,0,0]] 
# for i in range(len(X)):
#     for j in range(len(X[0])):
#         result[i][j] = X[i][j] + Y[i][j]
# print(result)

# X = [[10,11,12],[13,14,15],[16,17,18]] 
# Y = [[1,2,3],[4,5,6],[7,8,9]]
# result = [[0,0,0],[0,0,0],[0,0,0]] 
# for i in range(len(X)):
#     for j in range(len(X[0])):
#         result[i][j] = X[i][j] - Y[i][j]
# print(result)

# X = [[1, 2], [4, 5], [3, 6]] 
# Y = [[1,2,3,4],[5,6,7,8]]
# result = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]] 
# for i in range(len(X)):
#     for j in range(len(Y[0])):
#         for k in range(len(Y)):
#             result[i][j] += X[i][k] * Y[k][j]

# for r in result:
#     print(r)

# Employees =[{"name":"John Mckee", "age":38, "Department":"Sales"},\
#     {"name":"Lisa Crawford","age":29,"Department":"Marketing"},{"name":"Sujan Patel","age":28,"Department":"HR"}]
# for Employee in Employees:
#     print("Name: ", Employee["name"])
#     print("Age: ", Employee["age"])
#     print("Dept: ", Employee["Department"])
#     print('-'*20)

# orders = {'apple':5, 'orange':3, 'banana':2} 
# print(orders.values()) 
# print(list(orders.values()))


# s3 = set([3,4,5,6,6,6,1,1,2]) 
# print(s3)

# l = [5, 8, 1, 3, 2] 
# still_swapping = True

# while still_swapping:    
#     still_swapping = False    
#     for i in range(len(l) - 1):        
#         if l[i] > l[i+1]:            
#             l[i], l[i+1] = l[i+1], l[i]            
#             still_swapping = True

# print(l)

# search_for = 10
# result = -1
# for i in range(len(l)):    
#     if search_for == l[i]:        
#         result = i
#         print(result)       
#         break
#     else:
#         print("Not Found")


# l = [2, 3, 5, 8, 11, 12, 18]
# search_for = 3
# slice_start = 0 
# slice_end = len(l) - 1 
# found = False
# while slice_start <= slice_end and not found:    
#     location = (slice_start + slice_end) // 2    
#     if l[location] == search_for:        
#         found = True    
#     else:        
#         if search_for < l[location]:            
#             slice_end = location - 1        
#         else:            
#             slice_start = location + 1 

# print(found) 
# print(location)

# def sum_first_n(n):    
#     result = 0    
#     for i in range(n):        
#         result += i +1    
#     print(result)

# sum_first_n(10)

# def print_the_next_number(start):        
#     print(start + 1)        
#     return print_the_next_number(start + 1) 
# print_the_next_number(5)

# def print_the_next_number(start):    
#     print(start + 1)    
#     if start >= 7:        
#         return "I'm bored"    
#     return print_the_next_number(start + 1)

# print_the_next_number(5)

# def countdown(n):    
#     if n == 0:        
#         print('liftoff!')    
#     else:        
#         print(n)        
#         return countdown(n - 1)
# countdown(5)

# names = ['Magda', 'Jose', 'Anne']

# lengths = [] 
# for name in names:    
#     lengths.append(len(name))

# lengths = list(map(len, names))

# m=input("Please create a password: ")

# for i in m 
#     if
# password_=[]

import re
# phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d') 
# mo = phoneNumRegex.search('My number is 415-555-4242.')
# print('Phone number found: ' + mo.group()) 

phoneRegex= re.compile(r'''(
    (\d{3}|\(\d{3}\))?
    (\s|-|\.)?
    (\d{3})
    (\s|-|\.)
    (\d{4})
    (\s*(ext|x|ext.)\s*(\d{2,5}))
)''',re.VERBOSE)

text='457-687-1458 ext 85 '

me=phoneRegex.findall(text)
print(me)
# matches = [] 
# for groups in phoneRegex.findall(text):    
#     phoneNum = '-'.join([groups[1], groups[3], groups[5]])    if groups[8] != '':        phoneNum += ' x' + groups[8]    matches.append(phoneNum)