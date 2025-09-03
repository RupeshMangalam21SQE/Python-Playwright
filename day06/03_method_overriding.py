class Vehicle:
    def __init__(self, brand):
        self.brand = brand

    def display_info(self):
        print(f"Brand: {self.brand}")

class Car(Vehicle):
    def __init__(self, brand, num_doors):
        super().__init__(brand)
        self.num_doors = num_doors

    def display_info(self):
        print(f"Brand: {self.brand}, Doors: {self.num_doors}")

class Motorcycle(Vehicle):
    def __init__(self, brand, has_sidecar):
        super().__init__(brand)
        self.has_sidecar = has_sidecar

    def display_info(self):
        print(f"Brand: {self.brand}, Sidecar: {self.has_sidecar}")

car1 = Car("Toyota", 4)
bike1 = Motorcycle("Harley-Davidson", False)

car1.display_info()
bike1.display_info()
