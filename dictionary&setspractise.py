# # 1. make a dictionary with key being nepali words and values being their translation in english and ask user 
# mydist={"haat":"hand",
# "ankha":"eye",
# "ghar":"house"
# }
# print("options are:",mydist.keys() )
# a=input("Enter nepali word:")
# # print("The translation of your searched word is:",mydist[a])
# print("The translation of your searched word is:",mydist.get(a)) #much preferred here, [a]= .get(a)




# # 2 program to input 8 numbers from user and display unique numbers
# n1=input("Number no.1=")
# n2=input("Number no.2=")
# n3=input("Number no.3=")
# n4=input("Number no.4=")
# n5=input("Number no.5=")
# n6=input("Number no.6=")
# n7=input("Number no.7=")
# n8=input("Number no.8=")
# list={n1,n2,n3,n4,n5,n6,n7,n8}
# print(list)




# # 3.can we have set of int(18) and str(18) answer:yes
# list={int(18)}
# list.add(str("18"))
# print(list)

# # OR
# list={18,"18",18.0}
# print(list)



# # 4. length 
# s=set()
# s.add(20)
# s.add(20.0)
# s.add("20")
# print(s)
# print(len(s))=>2



# # 5.type of s={} => dictionary
# s={}
# print(type(s))



# # 6.create empty dictionary and let user add 4 values using key as person names
# mydict={}
# f1=input("favourite word of sujan:")
# f2=input("favourite word of amit:")
# f3=input("favourite word of nirjal:")
# f4=input("favourite word of arpita:")
# mydict['sujan']=f1
# mydict['amit']=f2
# mydict['nirjal']=f3
# mydict['arpita']=f4
# print(mydict)



# 7. if two person has same name then python with only print value of 1st one and neglect 2nd same name(key)



# 8. if two values are same then both values will be printed i.e.values can be same but keys can't be same


