# # 1. create a class programmer for storing information of few programmers working at microsoft
# class Programmer:
#     company="Microsoft"
    
#     def __init__(self,name,address,salary):
#         self.name=name 
#         self.address=address
#         self.salary=salary
#     def getdetails(self):
#         print(f"The name of the employee is {self.name}, lives in {self.address} and receive salary {self.salary}")
#     def getSalary(self):
#         print(f"Salary of this employee is {self.salary}")

# sujan=Programmer("Sujan Sapkota", "kathmadu", 10000)
# arpita=Programmer("Arpita", "Australia", 150000)
# sujan.getdetails()
# arpita.getdetails()




# # 2. write a class calculator capable of finding square, cube and squareroot of a number:

# class Calculator:
    
#     def __init__(self, number):
#         self.number=number

#     def getoutput(self):
#         print(f'''The square of {self.number} is {self.number * self.number}\n
# The cube of {self.number} is {self.number * self.number * self.number}\n
# The squareroot of {self.number} is {self.number ** 0.5}''')
# num=Calculator(4)
# num.getoutput()




# 3. create a class with the class attribute a; create an object from it and set a directly using object.a=0. Does this change the class attribute

# class Class:
#     a=20
# object=Class()
# object.a=0
# print(Class.a)
# print(object.a)
# # Answer: Class attribute will not change  if you have to change class attribute use Class.a=0


# 4. add a static method in problem 2 to greet the user with hello

# class Calculator:
    
#     def __init__(self, number):
#         self.number=number

#     def getoutput(self):
#         print(f'''The square of {self.number} is {self.number * self.number}\n
# The cube of {self.number} is {self.number * self.number * self.number}\n
# The squareroot of {self.number} is {self.number ** 0.5}''')
    
#     @staticmethod
#     def greet():
#         print("Hello and welcome to the best calculator ")

# num=Calculator(4)
# num.greet()
# num.getoutput()



# 5. Write a class train which has methods to book a ticket, get status(no of seats) and 
# get fare infomation of trains running under nepal railways

# class Train():
#     def __init__(self, name, fare, seats):
#         self.name=name
#         self.fare=fare
#         self.seats=seats
#     def getstatus(self):
#         print(f"****The name of the train is {self.name}***")
#         print(f"    Number of seats available in this train is {self.seats}")
#     def getfare(self):
#         print(f">>>>>The price of one seat in {self.name} is Rs.{self.fare}<<<<<<<")

#     def bookticket(self):
#         if (self.seats>0):
#             print(f"Your ticket has been booked on {self.name} and your seat number is {self.seats}")
#             self.seats=self.seats-1
#         else:
#             print(f"Sorry, no ticket is available in {self.name}.Train is full, try another train")
#     def cancelTicket(self):
#         p
    
# janakpur=Train("janakpur express:3300", 100, 2)
# janakpur.getstatus()
# janakpur.getfare()
# janakpur.bookticket()
# janakpur.bookticket()
# janakpur.bookticket()
# janakpur.getstatus()




# 6. 