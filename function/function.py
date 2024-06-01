# # syntax
# def fun(a):
#     return "hello"

# a1="how is your day"
# fun1=fun(a1)
# print(fun1)



# write a program to greet a user "Good day" using function
# method 1
# def fun(a):
#     return "Good day,"

# a1=input("What is your name:")
# fun1=fun(a1)
# print(fun1,a1)

# # method 2
# def greet(name):
#     print("Good day,", name)
# greet("Sujan")
# # OR
# # name=input("What is your name:")
# # greet(name)

# # method 3
# def greet(name):
#     s= "good day"+ name
#     return s
# a=greet("harry")
# print(a)


# def average(marks):    #def is used while writing function 
#     average=(sum(marks)/len(marks)) #return means once values has been calculated the result obtained is sent back to the point where it came from
#     return average

# marks1 =  [45,65,89,98]
# average1 = average(marks1)

# marks2 =  [45,65,78,88]
# average2 = average(marks2)

# print(average1,average2)


# # here we are looking for user defined functions mysum is user defined functions
# def mysum(num1, num2):
#     return num1+num2

# s=mysum(6, 40)
# print(s)

'''default_arguments---default parameter value
----> when we define function like "def greet(name)" and we asked to "greet()" then it will throw error because we have not given value in greet 
,so to remove it we use default arguments 
for that, def greet(name="Stranger") is an example so when so value is assinged in greet i.e. "greet()" then it will automatically accept stranger as a value
and error won't occur
"basically this is used when you have not passed any value "
'''

def greet(name="Stranger"):
    print("Good day, "+ name) 

# greet()
# greet("sujan")