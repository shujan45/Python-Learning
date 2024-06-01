
# class Employee:
#     company="Google"
#     def getSalary(self):
#         print("Salary is 100000")


# sujan= Employee()
# sujan.getSalary() # Employee.getSalary(sujan) is the derived form of "sujan.getSalary()" 



class Employee:
    company="Google"
    def getSalary(self):
        print(f"Salary of this employee working in {self.company} is {self.salary}")

sujan= Employee()
sujan.salary=10000
sujan.getSalary()