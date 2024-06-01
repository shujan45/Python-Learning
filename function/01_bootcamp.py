# def message():
#     print("Hel1o python")
# message()



# def message(name):
#     print("Hel1o python",name)
# message('ram')
# message('shyam')



# def add(a,b):
#     print(f"the addition of {a} and{b} is {a+b}")
# def sub(a,b):
#     print(f"the substraction of {a} and{b} is {a-b}")
# def mul(a,b):
#     print(f"the multiplication of {a} and{b} is {a*b}")
# add(10,12)
# sub(10,12)
# mul(10,12)


# def total(numbers):
#     sum = 0
#     for num in numbers:
#         sum+=num
#     print(sum)
# total([1,2,3,4,5,6])



# a,b,*c=1,2,3,4,5,6
# print(a)
# print(b)
# print(c)



# * arguments
# ** keyword arguments

# 
# def total(*numbers,**data):
#     print(numbers)
#     print(data)

# total(1,2,3,4,5,6,7,8,9,name='ram',phone=40)



# recursive function

# def hello():
#     print("Hello python")
# hello()


# def factorial(num):
#     if num==1:
#         return 1
#     else:
#         return num*factorial(num-1)
# print(factorial(5))

# def a():
#     return 120
# def b():
#     print(a())
# b()



# def add(x,y):
#     return x+y
# def total(a,b,callback):
#     print(callback(a,b))
# total(40,60,add)


# # simple interest from function
# def take_value():
#     p=int(input("Enter p:"))
#     t=int(input("Enter t:"))
#     r=int(input("Enter r:"))
#     return [p,t,r]
# def cal():
#     a,b,c=take_value()
#     return a*b*c/100

# def display():
#     print(cal())
# # cal()
# display()



# def add():
#     def total(x,y):
#         return x+y
#     return total

# # sm=add()
# # print(sm(5,8)) or

# print(add()(5,8))