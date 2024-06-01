# import requests

# url = requests.get('https://jsonplaceholder.typicode.com/users')
# data = url.json()
# print(data)


import re

# name='Ram123'
# patterns='^[a-zA-Z0-9\s]+$'

# if re.match(patterns,name):
#     print('valid')
# else:
#     print("invalid")



# phone='9840351059'
# patterns='^\d{10}$'

# if re.match(patterns,phone):
#     print('valid')
# else:
#     print("invalid")


# # another method
# phone=984035105
# patterns="^[0-9]{10}$"


# if re.match(patterns,str(phone)):
#     print('valid')
# else:
#     print("invalid")


# course='we are learning python'
# course=course.replace('python','java')
# print(course)


# a=5
# b=6
# c=a
# print(a)
# print(b)
# print(c)
# print(id(a))
# print(id(b))
# print(id(c))


dengue=float(input('enter your body temperature:'))
if dengue==103.33:
    print("you have dengue")
else:
    print("You are dengue free")
