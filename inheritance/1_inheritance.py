class Employee:
    company="Google"
    def getDetails(self):
        print("This is an employee:")

class Programmer(Employee):
    language="Python"
    company="Youtube"
    def getLang(self):
        print(f"The language is {self.language}")
    def getDetails(self):
        print("This is an employee who is programmer")

e=Employee()
p=Programmer()
e.getDetails()
print(p.company)
p.language="Java"
p.getLang()
p.getDetails()
