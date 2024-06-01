# class Person:
#     country='Nepal'
#     city="Kathmandu"
    
#     def __init__(self):
#         print("Initializing person...........")

#     def takeBreath(self):
#         print("I am breathing.........")

# class Employee(Person):
#     company="Honda"

#     def __init__(self):
#         super().__init__()
#         print("Initializing Employee...........")
    
#     def getSalary(self):
#         print(f"salary is {self.salary}")
    
#     def takeBreath(self):
#         print("I am an employee and luckily breathing....")

# class Programmer(Employee):
#     company="fiverr"
#     def __init__(self):
#         super().__init__()
#         print("Initializing programmer............. ")
    
#     def getSalary(self):
#         print("no salary to programmer........")
#     def takeBreath(self):
#         super().takeBreath() 
#         print("I am employee and breathing +++")    

# # p=Person()
# # p.takeBreath()


# # e=Employee()
# # # e.takeBreath()

# pr=Programmer()
# # pr.takeBreath() # it will use programmer if takeBreath is present and of employee(not programmer) and of person(if not inprogrammer and employee) 





class Person:
    country="Nepal"
    city="Kathmandu"
    def __init__(self):
        print("this is for person:")
    def read(self):
        print("Person always read to get knowledge:")

class Child(Person):
    gender="Boy"

    def __init__(self):
        print("This is for child....")
    def cry(self):
        super().read()
        print("Small child is crying:")

class Toy(Child):
    type="flying"
    def Num(self,num):
        super().cry()
        print(f"The number of toy played by child is {num}")


# p=Person()
# c=Child()
n=Toy()
n.Num(30)
# n.Num(30)