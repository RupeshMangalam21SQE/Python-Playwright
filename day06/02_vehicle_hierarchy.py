class Vehicle:
    def __init__(self, brand):
        self.brand = brand

class Car(Vehicle):
    def __init__(self, brand, num_doors):
        super().__init__(brand)
        self.num_doors = num_doors

class Motorcycle(Vehicle):
    def __init__(self, brand, has_sidecar):
        super().__init__(brand)
        self.has_sidecar = has_sidecar

car1 = Car("Toyota", 4)
bike1 = Motorcycle("Harley-Davidson", True)

print(car1.brand, car1.num_doors)
print(bike1.brand, bike1.has_sidecar)