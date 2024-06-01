# #1. program to find the greatest in three numbers using function
 
# def numbers(a,b,c):
#     if a>b and a>c:
#         # print(a ,"is greatest")
#         return a
#     elif b>c and b>a:
#         # print(b ,"is greatest")
#         return b
#     else:
#         # print(c ,"is greatest")
#         return c

# s=numbers(45, 23, 10)
# print("The greatest number is", s)



# #2. formula to convert celsius into fahrenheit

# def conversion(n):
#     F= (n * 9/5) + 32 
#     return F 
# s=conversion(1)
# print("Fahrenheit temperature is",s)


# #3. how to prevent python to print new line at the end
# '''by default "end" in a print has value "\n"'''
# print("How",end=" ")
# print("are", end=" ")
# print("u?", end=" ")



# #4. write a recurisive function to find the sum of first n natural number
# def natural(n):
#     if n==0:
#         return 0
#     return n + natural(n-1)
# s=natural(3) 
# print("the sum is",s)




# # 5. write a python function to print first n lines of following pattern
# '''
# * * *
# * *
# *
# '''
# def function(n):
#     for i in range(n):
#         print("* " * n)  
#         n=n-1
#         # or print("* " * n-i)
# s=function(3)




# # 6. write a program which converts inches into cm
# def converts(n):
#     s=n*2.54
#     return s
# p=converts(5)
# print(p)



# 7. write a program to remove a given word from a string n strip it at the same time
# a ="       sujan sapkota reads in phoenix college    "
# print(a)
# print(a.strip())

#8. write a program to print multiplication table of a given number
def mul(n):
    for i in range(1,11):
        s=i * n
        print(f"{i}*{n}={s}")
        i=i+1
p=mul(int(input("input a number:")))
