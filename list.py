# # List
# list is a collectionof data
# list is a mutable
# list is a ordered
# list is a iterable
# list is a indexable



a=["arpita","poudel","sujan","sapkota",0,1] #list is created with [] 
print(type(a))
# print(dir(a))


# print(a) 
# print(a[0]) #this will print the element of list having 0 index
# a[0]="names" #you can change the elements of list as well
# print(a) #this will print new list with "name" in it





# list slicing
name=["sujan","suraj","arpita","k18","arjun",'kedar','poudel']
print(name[1:6:2])





# b=[22,3,2,10,79,25,17,0]
# b.sort() #done to sort data in ascending order
# b.sort(reverse=True) #done to sort data in descending order
# print(b)
# b.reverse()
# b.append(20) # adds element at the end of list 
# b.insert(1,20) #inserts 20 at index 1 i.e. b.insert(index,elements_to_be_added)
# b.pop()
#b.pop(2) #this will take out element from index provided i.e b.pop(index) from list
#b.remove(10) #this will 20 from list i.e. b.remove(elements)
# print(b)



data=["sujan","hari","none"]
data1=['shyam','sita']
# data.extend(data1) #this won't have array from data1 and only provide values/elements
# data.append(data1)
# print(data)
print(data[2][0])


# data=[
#     1,2,3,[[[45]],78]
# ]

# print(data[3][0][0][0]) #this will print 45
# print(data[3][0][0][0],data[3][1]) #this will print 45 and 78 in same line
# print(data[3][1]) #this will print 78



students=[
    'ram','sita',
    'gita','hari',
    'sujan','abc'
]
print(len(students))
students.remove('ram')
print(students)
print(len(students))

