class RailwayForm:
    formType= "RailwayForm"
    def printData(self):
        print(f"Name is {self.name}")
        print(f"Train is {self.train}")
        print(f"Time is {self.time}")

sujanApplication = RailwayForm()
sujanApplication.name= "Sujan Sapkota"
sujanApplication.train="Janakpur Express"
sujanApplication.time="12:00"
sujanApplication.printData()
print("\n")
sudarshanApplication =RailwayForm()
sudarshanApplication.name="Sudarshan Sapkota"
sudarshanApplication.train="janakpur express"
sudarshanApplication.time="1 pm"
sudarshanApplication.printData()