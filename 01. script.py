class Dog:
    def __init__(self, name, breed, owner):
        self.name = name
        self.breed = breed
        self.owner = owner
    def bark(self):
        print("Woof! whoof!")

class Owner:
    def __init__(self, name, address, contact_number):
        self.name = name
        self.address = address
        self.contact_number = contact_number

    def walk_dog(self):
        print(f"{self.name} is walking {self.dog.name}")

owner1 = Owner("Dany", "123 Main St", "123-456-7890")
dog1 = Dog("Bruno", "Bulldog", owner1)
dog1.bark()  # Woof! whoof!
print(dog1.name)  # Bruno
print(dog1.breed)  # Bulldog
print(dog1.owner.name)

owner2 = Owner("Alice", "456 Main St", "132-465-7890")
dog2 = Dog("Fido", "Poodle", owner2)
print(dog2.owner.name)  # Alice
dog2.owner.walk_dog()  # Alice is walking Fido
 
'''
A class is like a blueprint for creating objects. An object is an instance of a class. The __init__ method is a special method in Python that is called when an instance of a class is created.
The __init__ method is used to initialize the attributes of a class. It is called with the class name followed by the arguments that are passed to the __init__ method. The __init__ method is called automatically when an instance of a class is created.

An object is an instance of a class. An object is created by calling the class name followed by the arguments that are passed to the __init__ method. The __init__ method is called automatically when an instance of a class is created.

Methods are functions that are defined inside a class. Methods are used to perform operations on the attributes of a class. Methods are called with the object name followed by the method name.

self refers to the instance of the class. It is used to access the attributes and methods of the class. self is passed as the first argument to the __init__ method and all other methods of the class.

 In the above code, we have two classes,  Dog  and  Owner . The  Dog  class has an  __init__  method that initializes the name, breed, and owner of the dog. The  bark  method prints the sound of the dog. The  Owner  class has an  __init__  method that initializes the name, address, and contact number of the owner. The  walk_dog  method prints the owner’s name and the dog’s name. 
 We have created two instances of the  Owner  class, owner1 and owner2, and two instances of the  Dog  class, dog1 and dog2. We have passed the owner1 instance to the dog1 instance and owner2 instance to the dog2 instance. 
 We have called the  bark  method of the dog1 instance, which prints the sound of the dog. We have also printed the name, breed, and owner’s name of the dog1 instance. 
 We have printed the owner’s name of the dog2 instance. We have called the  walk_dog  method of the owner2 instance, which prints the owner’s name and the dog’s name. 
 Conclusion 
 In this article, we have learned about the Python  __init__  method. We have seen how to use the  __init__  method to initialize the attributes of a class. We have also seen how to create instances of a class and pass arguments to the  __init__  method. 
 The  __init__  method is a special method in Python that is called when an instance of a class is created.
 '''