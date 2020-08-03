carplates=["ABC256","GHS547","YAD493","SEK970","WQJ981"]
odd_days=["MO","WE","FRI"]
even_days=["TU","TH","SA"]
pass_plate=[]

user_plate=input("Please enter your the number plate of your car: ")
user_day= input("What is today (SUnday - SAturday): ")

carplates.append(user_plate)
print("These are the car that are allowed to use the road today")
for plate in carplates:
    
    last_digit=int(plate[-1])
    if user_day in odd_days and last_digit %2 != 0:
        pass_plate.append(plate)
    elif user_day in even_days and last_digit % 2 ==0:
        pass_plate.append(plate)
    elif user_day=="SU":
        pass_plate.append(plate)
print(*pass_plate, sep="\n") 