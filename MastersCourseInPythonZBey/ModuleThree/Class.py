class Car:
    def __init__(self,make, model, color):
        self.make = make
        self.model = model
        self.color = color
    
    def drive(self):
        print(f"{self.make} {self.model} is driving")
    
    def stop(self):
        print(f"{self.make} {self.model} is stopping")
    

my_car = Car("Ford", "Mustang", "Red")
print(my_car.make)
print(my_car.model)
print(my_car.color)
my_car.drive()
my_car.stop()