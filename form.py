import json

questions =[]
def request_question():
    while True:
        question={}
        is_new = input("Enter your question: \n\t")
        question["query"]= is_new

        is_type= input("Choose question type: \n ('text', 'choice', 'email', 'phone')\n\t")
        if is_type not in ['text', 'choice', 'email', 'phone']:
            print("please choose the right type")
            is_type= input("Choose question type: \n ('text', 'choice', 'email', 'phone')\n\t")
            question["type"]=is_type
        else:
            question["type"]=is_type

        questions.append(question)

        is_exit= input("Do you want to add another question 'y' for yes and 'n' for no:  ")
        if is_exit=="y":
            # is_new= input("Enter your question: \n\t")
            request_question()
        else:
            break
        break

            

request_question()
        
        
def save_form():
    with open("form_name.json","w") as f:
        json.dump(questions,f)

save_form()


