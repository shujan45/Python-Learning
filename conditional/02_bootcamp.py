# # cd = 100
# # 1-10
# # ntc to ntc - 2.5
# # ntc to ncell - 3.5
# # ncell to ncell - 1
# # ncell to ntc - 5
# connection=int(input('''Which connection you want to establish?
# 1. ntc to ntc
# 2. ntc to ncell
# 3. ncell to ncell
# 4. ncell to ntc
# Enter either 1,2,3 or 4::'''))
# if connection<=4:
#     call_duration=int(input("Call duration="))
#     if call_duration>100:
#         print("exceed limit:")
#     elif call_duration<=10:
#         cost=call_duration*1
#         print("Total cost for the call is",cost)    
#     else:
#         if connection==1:
#             cost=call_duration*2.5
#             print("Total cost for the call is",cost)    
#         elif connection==2:
#             cost=call_duration*3.5
#             print("Total cost for the call is",cost)    
#         elif connection==3:
#             cost=call_duration*1
#             print("Total cost for the call is",cost)    
#         else:
#             cost=call_duration*5
#             print("Total cost for the call is",cost)
# else:
#     print("Invalid Connection")





# 27km
# 0-5 k-s 15rs 10%












# 3.# compuer bazar
# print(1.dell(rs:20000) 2. Toshiba(Rs:30000)
# 3. Mac(Rs: 50000)

# option: enter any option
#   enter quantity?

# delevery option
#   1.home (rs: 1000) 2. pickup(free)

# packing:
# 1.plastic(rs:500) 2. bag(1000) 3. gift box(rs: 5000)

# location:
# 1. ktm (13% tax)
# 2. btk (free)
# 3. ltp(free)
# total?
# total quantity?
# tax amount?
# grand total?
# 1.dell


# print("..........Welcome to COMPUTER BAZER.......")
# print('''......Following are the laptop available in our store.......
#     1. Dell---------->Rs.20000
#     2. Toshiba------->Rs 30000
#     3. Mac----------->Rs 50000
#     ''')

# option= int(input("Which laptop you are looking for? -- Choose 1 2 or 3:::::"))
# if option<=3:
#     quantity=int(input("How many laptop are you looking for?"))
#     if option==1:
#         price=quantity*20000
#     elif option==2:
#         price=quantity*30000
#     elif option==3:
#         price=quantity*50000
# else:
#     print("Please, Enter 1 or 2 or 3:::")
#     option= int(input("Which laptop you are looking for? -- Choose 1 2 or 3:::::"))


# delivery=int(input(('''How you want your laptop delivered?
# 1. Home delivery-------->Rs.1000
# 2. Pickup--------------->free 
#  ''')))
# if delivery==1:
#     price1=price+1000
# else:
#     exit
# packaing=int(input('''Which packaging would you prefer?
# 1. Plastic-------->Rs.500
# 2. bag------------>Rs.1000
# 3. Gift Box------->RS.5000
# :'''))
# if packaing==1:
#     totalprice=price1+500
#     print("Total price before adding tax is",totalprice)
# elif packaing==2:
#     totalprice=price1+1000
#     print("Total price before adding tax is",totalprice)
# elif packaing==3:
#     totalprice=price1+5000
#     print("Total price before adding tax is",totalprice)
# else:
#     print("Please provide 1,2 or 3 option only")
# place=int(input('''Where are you from?
# 1. kathmandu
# 2. baktapur
# 3. Lalitpur
# :'''))
# if place==1:
#     tax=13*price/100
#     print("The total amount of tax is", tax)
# else:
#     tax=0
# grandTotal=totalprice+tax
# print(f"total bill of your {quantity} laptop is {grandTotal}")





# # username=input("Enter the username:")
# # password=input("Enter the password:")
# '''# if username=='ram' and password=='ram002':
# #     print("Login success")
# # elif username=="ram" and password!="ram002":
# #     print("Wrong password")
# # elif username!="ram" and password=="ram002":
# #     print("Wrong username")
# # else:
# #     print("Invalid username and password")'''

# '''------------another way/method-----------'''
# username=input("Enter the username:")
# if username=="ram":
#     password=input("Enter the password:")
#     if password=="ram002":
#         print("login success")
#     else:
#         print("Password is incorrect")
#         exit()
# else:
#     print("username is incorrect")
#     exit()





# students=['ram','sita','hari','gita','sophia']
# name=input("Enter your name::")
# if name in students:
#     print("--------------->Student found<------------",name)
# else:
#     print("--------------->User not found<-----------",name)




# users=[
#     ['ram','ram002'],
#     ['shyam','shym002']
# ]

# username=input("Enter your username:")
# if users[0][0]==username or users[1][0]==username:
#     password=input("enter the password:")
#     if users[0][1]==password or users[1][1]==password:
#         print("login success")
#     else:
#         print("Wrong password")
# else:
#     print("user not found")






# 18-40 entrance
# 18-25 only coke
# 25-35 only fanta
# 35-40 only dew


age=int(input("Enter your age:"))
if age>=18 and age<=40:
    if age>=18 and age<25:
        print("You can have coke")
    elif age>=25 and age<35:
        print("You can have fanta")
    else:
        print("You can have dew")
else:
    print("You are not allowed in party")
