class Car:
    total_cars=0
    def __init__(self,b,m):
        self.brand=b
        self.model=m
        Car.total_cars+=1

    @classmethod
    def show_total(cls):
        print("Total mumber of cars created is",cls.total_cars)
    
    def display(self):
        print("Car_Name: ",self.brand)
        print("Car_model: ",self.model)

c1 = Car("Toyota", "Corolla")
c2 = Car("Tesla", "Model 3")
c3 = Car("Hyundai", "i20")

c1.display()
c2.display()

Car.show_total()