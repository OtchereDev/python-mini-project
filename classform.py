import json

class Form:
    
    def __init__(self):
        self.name = input('what is the name of the form: \n \t')
        self.questions=[]
        #self.request_question= request_question(self)

    def create(self):
        self.request_question()
        self.save_form()
    
    def request_question(self):
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

            self.questions.append(question)

            is_exit= input("Do you want to add another question 'y' for yes and 'n' for no:  ")
            if is_exit=="y":
                self.request_question()
            else:
                break
            break

            
    def save_form(self):
        form_name= self.name + ".json"
        with open(form_name,"w") as f:
            json.dump(self.questions,f)


kays_form= Form()

kays_form.create()