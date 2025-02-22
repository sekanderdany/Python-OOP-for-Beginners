class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def greet(self):
        print(f"Hello, my name is {self.name} and I am {self.age} years old.")

person1 = Person("Alice", 30)
person1.greet()  # Hello, my name is Alice and I am 30 years old.

person2 = Person("Bob", 25)
person2.greet()  # Hello, my name is Bob and I am 25 years old.



# In the above code, we have a class Person with an __init__ method that initializes the name and age of a person. We have created two instances of the Person class, person1 and person2, and passed the name and age of the person to the __init__ method. We have called the greet method of the person1 and person2 instances, which prints the name and age of the person.