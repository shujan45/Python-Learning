class Employee:
    company="Google"

    def __init__(self, name, salary, subunit):
        self.name=name
        self.salary=salary
        self.subunit=subunit
        print("Employee is created")

    def getdetails(self):
        print(f"The name of the employee is {self.name}")
        print(f"The salary of the employee is {self.salary}")
        print(f"The subunit of the employee is {self.subunit}")
    
    def getSalary(self, signature):
        
        print(f"Salary of this employee working in {self.company} is {self.salary}\n{signature}")
    
    @staticmethod
    def greet():
        print(f"Good morning, sir")

sujan = Employee("Sujan Sapkota",10000,"Printer")
# sujan =Employee() ----> this throws an error
# sujan.getdetails()
sujan.getSalary(100)