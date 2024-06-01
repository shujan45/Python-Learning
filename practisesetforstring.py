from datetime import date
from unicodedata import name


1 #program to ask user for name and print good afternoon with their's name 
 # a=input("Enter your name:")
# print("Good Afternoon," + a)



# 2 answer:
# letter = '''Dear <|Name|>,
# You are selected!,
# Date=<|Date|>
# '''
# name=input("enter your name:")
# date=input("enter the date:")
# letter=letter.replace("<|Name|>",name)
# letter=letter.replace("<|Date|>",date)
# print(letter)



3 #program to detect double spaces
#  # str="for finding double  spaces in given statement"
# doublespace=str.find("  ")
# print(doublespace)


4 # program to replace double spaces with single space
str="for finding double  spaces in given statement  and how are  you"
replace=str.replace("  "," ")
print(replace)


''' 5. write a program to formate the given details using escapesequences   
Dear Sujan, where are you now. Thanks! Yours AP'''
str="Dear Sujan,\n\tWhere are you now.\n\t\t\t\t\t\t\tThanks!\n\t\t\t\t\t\t\tYour\'s AP"
print(str)




str="Dear Sujan,\nWhere are you now.\nThanks!\nYour\'s AP"
print(str)