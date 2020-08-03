class Engineer():
    def __init__(self, license_no):
        self.license_no= license_no
    def design_project(self):
        print("I am working on this project")

class SeniorEngineer(Engineer):
    def __init__(self, license_no, num_projects):
        super().__init__(license_no)
        self.num_projects= num_projects
    def deal_project(self):
        print("I have got a deal project to do")
        self.num_projects += 1

class SnrComputerEngineer(SeniorEngineer):
    def __init__(self, license_no, num_projects,current_project):
        super().__init__(license_no,num_projects)
        self.current_project = current_project

leslie= Engineer("ABH256")
leslie.design_project()

cindy = SeniorEngineer("Ajdkf565", 5)
cindy.deal_project()
print("Now Cindy has handled "+ str(cindy.num_projects)+ " projects.")

terry= SnrComputerEngineer("pfgd564",6,"Movement")
print(terry.current_project)