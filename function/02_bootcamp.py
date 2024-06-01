import datetime
# from function import greet

# greet("sampanna")





# n_date =datetime.datetime(2001,8,20)
# today=datetime.datetime.today()
# print("",today-n_date)



# n_date =datetime.datetime(2023,8,20)
# today=datetime.datetime.today()
# print("Your birthday is due in",n_date-today)


# jobs =[
#     {'title':'python developer','exp_date':'2022-05-21'},
#     {'title':'java developer','exp_date':'2024-05-21'},
#     {'title':'php developer','exp_date':'2021-05-21'},
# ]

# for i in jobs:
#     exp =i['exp_date']
#     exp_date=datetime.datetime.strptime(i['exp_date'],'%Y-%m-%d')
#     today=datetime.datetime.now()
#     if exp_date>=today:
#         print(f"You can still apply for {i['title']}" )
#     else:
#         print(f"Due date is gone for {i['title']}")




today=datetime.datetime.now()
start_date=input("When your exam starts?")
start__date=datetime.datetime.strptime(start_date, '%Y-%m-%d')
print("Your exam will start in",start__date-today)
print("----------------------------------------------------")
end_date=input("When your exam end?")
end__date=datetime.datetime.strptime(end_date, '%Y-%m-%d')
print("Your exam will end in",end__date-today)
