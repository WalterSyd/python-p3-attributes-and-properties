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
    def __init__(self, name="Guok", breed="Mastiff"):
        # Initialize private variables for getter & setter methods
        self._name = None
        self._breed = None
        # Use the setter to validate the name
        self.name = name
        self.name = name
        
    

#Get setter for name
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


#Get setter for breed
    @property
    def breed(self):
        return self._breed
    
    @breed.setter
    def breed(self, value):
        if value in APPROVED_BREEDS:
            self._breed = value
        else:
            print("Breed must be in list of approved breeds.")

dog = Dog("Snoopy", "Beagle")
print(dog.name) 
print(dog.breed) 


dog.name = "A really long name that exceeds the limit"  # Output: Name must be string between 1 and 25 characters.
print(dog.name)  

