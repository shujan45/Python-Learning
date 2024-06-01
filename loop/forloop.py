# list=[1,2,3,4,5,6,7,8,9]
# print(list)
# for items in list:
#     print(items)
# print("done")


# # <------ Range in python------>
# for items in range(8): #range's value goes to n-1 where n=0
#     # print(items,end="done\n")
#     # print("Done")
#     print(items, end='done')


# for items in range(1,8): #range's value goes to n-1 where n=1
#     print(items)


''' Range formate in python is "(start, stop, step-size)" i.e if range(0,10,1) is given
    value start at 1 and ends at 9(since, it goes to n-1) and the difference is 1 between two numbers
if range is (8) then start will be automatically 0 and step-size will be 1
    '''

# for i in range(1,10,3): #here after 1 is printed then two numbers are skiped and so on:
#     print(i)




# # <--------for with else------>
# for i in range(9):
#     print(i)
# else:    
#     print("done")  

# # OR
# for i in range(9):
#     print(i)
# print("done")



# # <-----break statement---->
# for i in range(10):
#     print("This is ",i)
#     if i==5 :
#         print("this is different than other", i)
#         break
# else:
#     print("Our job is done")   #"else" in loop is applied when "for" does/complete its part
#     '''Here "for loop" is not completed because break is appiled through "if statement" so,
#       print part of else statement is not printed  '''

# for i in range(10):
#     if i==5:  
#         print("This is different", i)
#         break
#     print("This is",i)
# else:
#     print("I am Done")    


# # <--------continue-------->
# for i in range(10):
#     if i==5:
#         print("This", i, "is different")
#         continue #continue statement continue the loop after breaking that "condition of if statement"
#     print("This is ",i) 
#     '''here 0,1,2,3,4 is printed and since if has i==5 so "continue" will cotinue to print other than 5
#       basically "continue"  does  not care below it '''


# for i in range(0,20): #(0,20)   gives same meaning as (20)
#     if i%2==0:
#         continue
#     print("this old number is",i)




# # <------------pass statement--------->
# i = 4
# if i>0:
#     print("This is",i)
#     pass #it instruct to do nothing ,pass is a null statement in python
# while i>2:
#     pass
# print("Done")