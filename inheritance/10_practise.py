# # 1. create a class  C-2d vector and use it to create another class representing a 3-d vector
# class C2dVec:
#     def __init__(self, i,j):
#         self.icap=i
#         self.jcap=j

#     def __str__(self):
#         return f"{self.icap}i + {self.jcap}j"

# class C3dVec(C2dVec):
#     def __init__(self, i , j, k):
#         super().__init__(i,j)
#         self.kcap=k
    
#     def __str__(self):
#         return f"{self.icap}i + {self.jcap}j + {self.kcap}k"



# v2d = C2dVec(1, 3)
# v3d = C3dVec(1, 9, 7)
# print(v2d)
# print(v3d)




# #2. Create a class pets from a class Animals and further create class Dog from Pets. Add a method back to class Dog

# class Animals:
#     animalType="Mamal"
    

# class Pets(Animals):
#     color="White"

# class Dog(Pets):
#     @staticmethod
#     def bark():
#         print("Bow Bow!")

# d=Dog()
# d.bark()



# ''' 3. create  a class Employee and add salary and increment properties to it.
# Write a method salaryAfterIncrement method with  a @property decorator with a setter which changes the value of increment based on the salary'''

# class Employee:
#     salary= 5000
#     increment = 1.5
#     @property
#     def salaryAfterIncrement(self):
#         return self.salary * self.increment
#     @salaryAfterIncrement.setter
#     def salaryAfterIncrement(self,val):
#         self.increment = val/self.salary
# e=Employee()
# print(e.salaryAfterIncrement)
# print(e.increment)

# e.salaryAfterIncrement=10000
# print(e.increment)




# 4. Write a class complex to represent complex numbers along with overloaded opertors + and * which adds and multipies them
# complex number multiplication, (a+bi)(c+di)=(ac-bd)+(ad+bc)i  "concept of real and imaginary number"

# class Complex:
#     def __init__(self, r, i):
#         self.real=r 
#         self.imaginary =i
#     def __add__(self,c):
#         return Complex(self.real+c.real, self.imaginary+c.imaginary)
    
#     def __mul__(self,c):
#         mulReal=self.real*c.real -self.imaginary*c.imaginary
#         mulImg=self.real*c.imaginary+self.imaginary*c.real
#         return Complex(mulReal, mulImg)

#     def __str__(self):
#         return f"{self.real}+{self.imaginary}i"

# c1=Complex(1,4)
# c2=Complex(8,5)
# print(c1+c2)
# print(c1*c2)



# # 5. write a class vector representing a vector of n dimension. Overload the + and * operator which calculates the sum and the dot product of them.

# class Vector:
#     def __init__(self,vec):
#         self.vec=vec
#     def __str__(self):
#         str1= ""
#         index=0
#         for i in self.vec:
#             str1 += f" {i}a{index} +"
#             index += 1
#         return str1[:-1]
    
#     def __add__(self, vec2):
#         newList= []
#         for i in range(len(self.vec)):
#             newList.append(self.vec[i] + vec2.vec[i])
#         return Vector(newList)
    
#     def __mul__(self,vec2):
#         sum =0
#         for i in range (len(self.vec)):
#             sum += self.vec[i] * vec2.vec[i]
#         return sum
                
    
# v1=Vector([1,4])
# v2=Vector([1,6])
# print(v1*v2)



# 6. write __str__() method to print the vector as follows:
#   