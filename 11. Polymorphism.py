# Polymorphism

class Vehicle:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year

    def start(self):
        print("Vehicle is starting")

    def stop(self):
        print("Vehicle is stopping")


class Car(Vehicle):
    def __init__(self, brand, model, year, number_of_doors):
        super().__init__(brand, model, year)
        self.number_of_doors = number_of_doors

    def start(self):
        print("Starting the car")

    def stop(self):
        print("Stopping the car")


class Motorcycle(Vehicle):
    def __init__(self, brand, model, year):
        super().__init__(brand, model, year)

    def start(self):
        print("Starting the motorcycle")

    def stop(self):
        print("Stopping the motorcycle")


class Plane(Vehicle):
    def __init__(self, brand, model, year):
        super().__init__(brand, model, year)

    def start(self):
        print("Starting the plane")

    def stop(self):
        print("Stopping the plane")


vehicles: list[Vehicle] = [
    Car("Toyota", "Camry", 2020, 4),
    Motorcycle("Yamaha", "MT-07", 2021),
    Plane("Boeing", "747", 2019)
]

# Step 3 loop
for vehicle in vehicles:
    print(
        f"Vehicle: {vehicle.brand} {vehicle.model}, Year: {vehicle.year} ({type(vehicle).__name__})")
    vehicle.start()
    vehicle.stop()
# Step 2 loop
# for vehicle in vehicles:
#     if isinstance(vehicle, Vehicle):
#         print(f"Vehicle: {vehicle.brand} {vehicle.model}, Year: {vehicle.year} ({type(vehicle).__name__})")
#         vehicle.start()
#         vehicle.stop()

# Step 1 loop
# loop through list of vehicles to inspect them
# for vehicle in vehicles:
#     if isinstance(vehicle, Car):
#         print(
#             f"Car: {vehicle.brand} {vehicle.model}, Year: {vehicle.year}, Doors: {vehicle.number_of_doors}")
#         vehicle.start()
#         vehicle.stop()
#     elif isinstance(vehicle, Motorcycle):
#         print(
#             f"Motorcycle: {vehicle.brand} {vehicle.model}, Year: {vehicle.year}")
#         vehicle.start()
#         vehicle.stop()
#     else:
#         raise Exception("Unknown vehicle type")


# In the above code, we have a base class Vehicle with an __init__ method that initializes the brand, model, and year of the vehicle. We have two subclasses, Car and Motorcycle, that inherit from the Vehicle class. Both subclasses override the start and stop methods to provide their own implementations. We create instances of the Car and Motorcycle classes and call their start and stop methods.
# Polymorphism allows us to use a single interface to represent different types of objects. In this case, we can use the Vehicle class as a common interface for both Car and Motorcycle classes, allowing us to call the start and stop methods on any vehicle object without knowing its specific type.
