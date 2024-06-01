c=set()
c.add(4) # adding elements in empty set
c.add(5)
# c.add([1,2,3]) #throws error as lists can't be add in sets as it can be changed
c.add((1,9,8,7,6)) #tuples can be added in sets as it can't be changed
# c.add({"sujan":"student"}) #cannot add dictionary as well
# print(c)


# print(len(c)) #length of this sets


# #c.remove(5) #removes 5 from set
# #c.remove(10) #throws an error as it can't remove bcz 10 is not in set
# print(c)

# # print(c.pop())
# # print(c)


print(c.union({1,9}))
print(c.intersection({1,9}))