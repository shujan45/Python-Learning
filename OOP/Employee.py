# # class Attributes

# class Employee:
#     company = "Google"
# sujan =Employee()
# arpita =Employee()
# print(sujan.company)

# Employee.company ="Youtube" #changing the name of attributes through class
# print(sujan.company)





# Instance Attributes(<>)
class Employee:
    company = "Google"
    salary = 10000
sujan =Employee()
arpita =Employee()


# creating instance attribute salary for both the objects
# sujan.salary=30000      #   <>
# arpita.salary = 40000   #   <>

print(sujan.company)

Employee.company ="Youtube" #changing the name of attributes through class
print(sujan.company)
print(sujan.salary)
print(arpita.salary)

# below line throws an error as address is not present in instance/class 
# print(sujan.address)