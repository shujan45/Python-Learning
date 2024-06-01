class Employee:
    company="camal"
    salary=100
    location="nepal"

    # def changeSalary(self, sal):
    #     self.__class__.salary=sal

    @classmethod
    def changeSalary(cls,salary):
        cls.salary=salary

e=Employee()
print(e.salary)
e.changeSalary(455)
print(e.salary)
print(Employee.salary)
print(e.salary)