class Employee:
    company="pepsi"
    salary=5000
    salaryBouns=500
    # totalSalary=5500

    @property
    def totalSalary(self ):
        return self.salary + self.salaryBouns

    @totalSalary.setter
    def totalSalary(self, val):
        self.salaryBouns = val - self.salary


e=Employee()
print(e.totalSalary)
# e.totalSalary()
e.totalSalary=40000
print(f"The bonus provided by the company is {e.salaryBouns}")
print(f"The salary provided by the company is {e.salary}")