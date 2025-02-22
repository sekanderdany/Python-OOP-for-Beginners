# Inheritance

class Vehicle:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year

    def start(self):
        print("Starting the vehicle")

    def stop(self):
        print("Stopping the vehicle")


class Car(Vehicle):
    def __init__(self, brand, model, year, number_of_doors, number_of_wheels):
        super().__init__(brand, model, year)
        self.number_of_doors = number_of_doors
        self.number_of_wheels = number_of_wheels


class Bike(Vehicle):
    def __init__(self, brand, model, year, number_of_wheels):
        super().__init__(brand, model, year)
        self.number_of_wheels = number_of_wheels


car = Car("Toyota", "Camry", 2020, 4, 4)
bike = Bike("Yamaha", "MT-07", 2021, 2)

print(car.__dict__)
print(bike.__dict__)
print(f"Car: {car.brand} {car.model}, Year: {car.year}, Doors: {car.number_of_doors}, Wheels: {car.number_of_wheels}")
print(f"Bike: {bike.brand} {bike.model}, Year: {bike.year}, Wheels: {bike.number_of_wheels}")
car.start()
bike.stop()


# In the above code, we have a base class Vehicle with an __init__ method that initializes the brand, model, and year of the vehicle. We have two subclasses, Car and Bike, that inherit from the Vehicle class. The Car class has an additional attribute number_of_doors, while the Bike class has an additional attribute number_of_wheels. We create instances of the Car and Bike classes and print their attributes.
# Inheritance allows us to create a new class that is a modified version of an existing class. The new class inherits the attributes and methods of the existing class, allowing us to reuse code and create a hierarchy of classes.
