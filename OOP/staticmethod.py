
# class Employee:
#     company="Google"
#     def getSalary(self, signature):
#         print(f"Salary of this employee working in {self.company} is {self.salary}\n{signature}")
    
#     @staticmethod
#     def greet():
#         print(f"Good morning, sir")

# sujan= Employee()
# sujan.salary=10000
# sujan.getSalary("Thanks!") # Employee.getSalary(sujan)
# sujan.greet()



# def add(x,y):
#     return x+y

# print (add(10,20))



# def add(x,y):
#     return x+y

# def total(a,b,func):
#     print(func)
#     return func(a,b)

# print(total(10,20,add))


# def message(any):
#     print(any())
# def user():
#     return"hello"

# message((user))



# def user():
#     def info():
#         print("Hello info")
#     return info
# user()()

# def user():
#     def info(name):
#         print("Hello,",name)
#     return info
# user()('sujan')



# def test():
#     return "h1"

# a=test
# print(a())



class Student:
    x=10
    @staticmethod
    def __init__(name):
        print(name)
    @staticmethod
    def hello():
        print("Hello")

Student('sujan').hello()