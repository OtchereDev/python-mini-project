black_list_student=["Richmond","Kelly","Efya","Jojo"]
num_students=int(input("Enter the the number of student: "))
white_list=[]
student_list=[]

for student in range(num_students):
    prompt=input("Enter a name of a student: ")
    while prompt == "":
        prompt=input("Enter a non-empty name: ")
    student_list.append(prompt)
for student in student_list:
    if student not in black_list_student:
        white_list.append(student)
print("These are "+ str(len(white_list))+ " student are graduating this year: ")
print(*sorted(white_list), sep="\n")