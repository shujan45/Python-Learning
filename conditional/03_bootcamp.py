# # a,b,c
# # d 
# # enter the numvber --user
# # a must be greater than b
# # a>b>c>d   
# # sabai condition milnhu paryo agadi jana lae
# a=int(input("Enter one number for value a:"))
# print(f"you have entered {a}")
# b=int(input("Enter anither number for value b:"))
# if b>a:
#     print("Congratulation:")
#     c=int(input("Enter another value for c:"))
#     if c>b:
#         print("Access granted:")
#         d=int(input("Enter for value d:"))
#         if d>c:
#             print("Permission granted")
#             print(a,b,c,d)
#         else:
#             print("C is greater than d")
#     else:
#         print("b is greater than c so that you can't enter")
# else:
#     print("A is greater than b, so exit")



# # for username only
# users=[
#     {'username':'ram'},
#     {'username':'hari'},
#     {'username':'sita'}
# ]
# userid=input("Enter the username:")
# if users[0]['username']==userid or users[1]['username']==userid or users[2]['username']==userid:
#     print("valid user")
# else:
#     print("user not found")



# for both username and password
users=[
    {'username':'ram',
    'password':'ram002'},
    {'username':'hari',
    'password':'hari002'},
    {'username':'sita',
    'password':'sita002'}
]
userid=input("Enter the username:")
if users[0]['username']==userid or users[1]['username']==userid or users[2]['username']==userid:
    # print("valid user::")
    password =input("Enter password:")
    if users[0]['password']==password or users[1]['password']==password or users[2]['password']==password:
        print("Permission granted::")
    else:
        print("Wrong password::")
else:
    print("user not found")