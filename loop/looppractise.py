# # 1. write a program to print multiplication table of the given numbers using for loop
# number=int(input("Enter a number"))
# for i in reversed(range(1,11)):
#     # print(str(number)+"*"+str(i)+"="+str(i*number))
#     print(f"{number}*{i}={number*i}")



# number=int(input("Enter a nummer"))
# for i in reversed(range(1,21)):
#     print(f"{number}*{i}={number * i}")

# num=int(input("enter a number:"))
# for i in range(1,11,2):
#     print(f"{num}*{i}={num * i}")


# # <---using while loop------>
# i=int(input("Enter a number"))
# j=1
# while j<=10:
#     print(f"{i}*{j}={i*j}")
#     j=j+1


# -------->        f"{}*{}={  *  }"


# # 2. program to greet all the person in the list
# l1=["Harry","Sohan","Sachin","Rahul"]
# for i in l1:
#     if i.startswith("S"):
#         print("Hello", i)



# # 4. Write a program to check if given number is prime or not
# num=int(input("Enter a num:"))
# Prime=True
# for i in range(2,num):
#     if(num%i==0):
#         Prime=False
#         break
# if Prime:
#     print("this number is prime number")
# else:
#     print("this number is not prime number")




# # 5. to find the find the factorial 
# num=int(input("Enter a number:"))
# factorial=1
# for i in range(1,num+1):
#     factorial=factorial*i
# print(f"The factorial of {num} is {factorial}")





# # pattern
# n=3
# for i in range(3):
#     print("*" * (i+1))



# ''' pattern with space
# __*__ 
# _***_
# ***** 
# '''
# n=3
# for i in range(3):
#     print("_" * (n-i-1),end="")
#     print("*" * (2*i+1),end="")
#     print("_" * (n-i-1))



# '''pattern 
# ***
# *_*
# ***
# '''
# n=3
# for i in range(3):
#     if i==1:
#         print("*"+" "+"*")
#         continue
#     print("*" * 3)








# # program to greet all person in the list

# #--------using while loop------------
# list=["sujan","paras","rohit","curry","arpita"]
# a=len(list)
# i=0
# # print(list[i])
# while i<a:
#     print("Good Morning,", list[i])
#     i=i+1


# print("--------------------------------------------------")

# # -----------for loop------------
# list=["sujan","paras","rohit","curry","arpita"]
# for i in list:
#     print("Good Morning,",i)