# n!=1*2*3*4*......   n
# n!=1*2*3*4*(n-1)*n
# n!=(n-1)!*n


# # to find factorial of 4
# n=4
# product =1
# for i in range (n):
#     product= product * (i+1)
# print(product)



# def factorial_iter(n):
#     product =1
#     for i in range (n):
#         product= product * (i+1)
#     return product

# s=factorial_iter(15)
# print(s)


# recursive function 
'''recursive is a function which calls itself. it is used directly use a mathematical formula as a function. '''
def factorial_recursive(n):
    if n==1 or n==0:
        return 1
    return n * factorial_recursive(n-1)
print(factorial_recursive(1))