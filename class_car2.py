class Car:
    def __init__(self,make,model,year):
        self.make = make
        self.model = model
        self.year = year
car1 = Car("toyota".title(),"RAV4",2024)
car2 = Car(input("enter car make ?"),input("enter model"),input("enter year"))
car3 = Car(input("enter car make ?"),input("enter model"),input("enter year"))
print("\n")
print(car1.make,car1.model,car1.year)
print(car2.make.title(),car2.model.upper(),car2.year)
print(car3.make.title(),car3.model.upper(),car3.year)
        
        
    