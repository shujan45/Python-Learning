# # <------while loop--------->
# i=0
# while i<10:     #while condition
#     print("yes") #body of the loop ---> if condition is true "body of the loop" is executed
#     '''here infinite loop is created until we change anything in the condition part 
#     for example,n above scenario yes is printed infinite times sonce 0<10 
#     '''
#     i=i+1 #now since we changed the condition once yes is printed for i=0, i=i+1 operation 
#         #is carried out changing the value of i to be 1 then it again checks the above condition i.e. i<10

# # print("Done") #once the condition "i<10" becomes false i.e. when i=10,
# #             #we come out of the loop and "done" is printed


# #Q= program to print from 1 to 50 using while loop
# i=1
# while i<=50:
#     print(i)
#     i=i+1
# print("Done")

# # using for loop 
# for i in range(1,51):
#     print(i)

# #Q= program to print the content of the list using while loop 
# list=["sujan","sapkota","9840","Rohit","Sharma","45"]
# # a=len(list)
# # print(a)
# i=0
# while i<len(list):
#     print(list[i])
#     i=i+1



# list= ["sujan","sapkota","paras","khadka","rohit","sharma","stephen","curry","arpita","poudel"]
# a=len(list)
# print(a)
# i=0
# while i<a:
#     print(list[i])
#     i=i+1