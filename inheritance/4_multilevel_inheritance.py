class Person:
    country='Nepal'
    city="Kathmandu"
    def takeBreath(self):
        print("I am breathing.........")

class Employee(Person):
    company="Honda"
    def getSalary(self):
        print(f"salary is {self.salary}")
    def takeBreath(self):
        print("I am an employee and luckily breathing....")

class Programmer(Employee):
    company="fiverr"
    def getSalary(self):
        print("no salary to programmer........")
    def takeBreath(self):
        print("I am employee and breathing +++")    

p=Person()
p.takeBreath()
# print("p.company") #this will throw an error 

e=Employee()
e.takeBreath()

pr=Programmer()
pr.takeBreath() # it will use programmer if takeBreath is present and of employee(not programmer) and of person(if not inprogrammer and employee) 
print(pr.country)