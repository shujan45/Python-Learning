# class Student:
#     x=10

#     def info(self):
#         print(self.x)
#         print("Hello")
# obj=Student()
# obj.info()




# class Calculator:
#     x=int(input("Enter a number 1:"))
#     y=int(input("Enter a number 2:"))
#     def add(self):
#         print("the addition is:",self.x+self.y)
#     def sub(self):
#         print("the substraction is:",self.x-self.y)
#     def mul(self):
#         print("The multiplication is:",self.x*self.y)
#     def divide(self):
#         print("The division is",self.x/self.y)

# cal=Calculator()
# cal.add()
# cal.sub()
# cal.mul()
# cal.divide()


# # another method
# class Calculator:
#     def add(Self,a ,b):
#         return a+b
#     def sub(Self,a ,b):
#         return a-b
#     def mul(Self,a ,b):
#         return a*b
#     def div(Self,a ,b):
#         return a/b
# cal=Calculator()
# x=int(input("Enter a number:"))
# y=int(input("Enter a number:"))
# print(cal.add(x,y))
# print(cal.sub(x,y))
# print(cal.mul(x,y))
# print(cal.div(x,y))


# class A:
#     def last_id(self):
#         return 245

# obj=A()
# obj.last_id()   #this doesnot provide any output
# print(obj.last_id()) #this provide 245 


# class SIP:
#     def take_value(self):
#         P=int(input("Enter value for principle:"))
#         T=int(input("Enter value for time:"))
#         R=int(input("Enter value for rate:"))
#         return[P,T,R]
#     def calculator(self):
#         a,b,c=self.take_value()
#         return a*b*c/100
#     def display(self):
#         print(self.calculator())
# obj=SIP()
# obj.display()


# class Students:
#     data=[
#         {'name':'Ram','age':'20','address':'kathmandu'},
#         {'name':'shyam','age':'21','address':'jitpur phedi'},
#         {'name':'hari','age':'23','address':'maitidevi'}
#     ]

#     def show(self):
#         return self.data
#     def get_by_name(self,search):
#         for items in self.data:
#             if items['name']==search:
#                 print(items)

#     def add(self,new_data):
#         self.data.append(new_data)
#         print(self.data)

# obj=Students()
# print(obj.show())
# obj.get_by_name('hari') 
# x={'name':'sujan','age':'21','address':'jitpur phedi' }
# obj.add(x)
# # print(Students.data)



# class College:
#     x=10
#     def test(self):
#         print(f"for the class and method")

# obj=College()
# print(obj.x)
# obj.test()

# # del =destructor and init = constructor (and are called special method) del and init jata rakhepani uniharu starting and end phase ma nai run hunxa
# class College:
#     def __del__(self):
#         print("Destructor")
#     def __init__(self):
#         print("Constructor")
#     def test(self):
#         print("This is test")
# obj=College()
# obj.test()




# class Students:
#     total=0
#     def __init__(self,name):
#         self.name=name
#         Students.total+=1

# obj=Students("ram")
# obj1=Students("shyam")
# obj2=Students("hari")
# print(obj.total)

