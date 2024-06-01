# #procedural programming
# a=14
# b=34
# print("The sum of a and b is", a+b)



# # object oriented programming
# class Number:
#     def sum(self):
#         return self.a + self.b
# num =Number()  #object instantiation
# num.a =12
# num.b = 34
# s=num.sum()
# print(s)


class Number:
    def sum(self,a,b,c=0):
        return a + b + c
num=Number()
s=num.sum(10,20,30)
print(s)
