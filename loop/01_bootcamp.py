# data =['ram','hari','shyam','gita']
# for name in data:
#     print(name)
#     print(name[0]) #this will print first letter of all element i.e. ram hari shyam gita



# data=[1,2,3,4,5,6,7,8,9,10,11,12,13]
# even_count=0
# odd_count=0
# for i in data:
#     if i%2==0:
#         even_count+=1
#     else:
#         odd_count+=1
# print("The total even numbers is",even_count)
# print("The total odd numbers is",odd_count)
        



# for i in range(1,11):
#     print(i,end='  ')
# print(end='\n')
# print("Reversed form")
# for i in reversed(range(1,11)):
#     print(i,end='  ')


# data=[
#     [1,2,3,4,5],
#     [6,7,8,9,10],
#     [11,12,13,14,15]
# ]

# for i in data:
#     for a in i:
#         print(a,end='  ')
    


# data=['ram','sita','gita','ram','ram']
# name=input("Enter your name:")
# count=0
# for i in data:
#     if i==name:
#         count+=1
#         print(i)
# print("Name you searched is",count)


# data=['ram','sita','gita','ram','ram']
# new_list=[]
# for i in data:
#     if i not in new_list:
#         new_list.append(i)
# print(new_list)


# for i in range(1, 11):
#     for j in range(1, 11):
#         result = i * j
#         print(f"{i} x {j} = {result}")
#     print()



# data=[
#     {'name':'ram','gender':'male'},
#     {'name':'gopal','gender':'male'},
#     {'name':'gita','gender':'female'},
#     {'name':'laxmi','gender':'female'},
#     {'name':'madan','gender':'male'},
# ]
# male_count=0
# female_count=0
# for i in data:
#     if i['gender']=='male':
#         male_count+=1
#     else:
#         female_count+=1
# print("The total number of male is:",male_count)
# print("The total number of female is:",female_count)
# print("total no of people:",male_count+female_count)



# # while
# x=1
# num=int(input('Enter a number:'))
# while x<=num:
#     print("hello python")
#     x+=1


data=[1,2,3,4,5,6,7,8]
x=0
while x<len(data):
    print(data[x])
    x+=1