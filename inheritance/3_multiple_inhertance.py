# Multiple Inheritance:-> multiple inheritance occurs when child class inherits from more than one parent class
class Employee:
    company="Visa"
    ecode= 120
class Freelancer:
    company="fiverr"
    level=0
    def upgradeLevel(self):
        self.level=self.level +1
class Programmer(Employee, Freelancer):
    name="sujan"
p=Programmer()
p.upgradeLevel()
print(p.company) #the first parent class (Employee, Freelancer) is printed, here employee is placed ahead of freelancer 
print(p.level)

print(
    "The outcome is the process that deals with g"
)