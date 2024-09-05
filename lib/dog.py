#!/usr/bin/env python3

APPROVED_BREEDS = [
    "Mastiff",
    "Chihuahua",
    "Corgi",
    "Shar Pei",
    "Beagle",
    "French Bulldog",
    "Pug",
    "Pointer"
]

class Dog:
    def __init__(self, name="Guok"):
        # Initialize a private variable
        self._name = None
        # Use the setter to validate the name
        self.name = name
    
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, value):        
        #a built-in Python function that checks if an object is an instance of a particular class.
        if isinstance(value, str) and 1 < len(value) <= 25:
            self._name = value
        else:
            print("Name must be string between 1 and 25 characters.")

dog = Dog("Snoopy")
print(dog.name)  


dog.name = "A really long name that exceeds the limit"  # Output: Name must be string between 1 and 25 characters.
print(dog.name)  
