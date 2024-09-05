#!/usr/bin/env python3

APPROVED_JOBS = [
    "Admin",
    "Customer Service",
    "Human Resources",
    "ITC",
    "Production",
    "Legal",
    "Finance",
    "Sales",
    "General Management",
    "Research & Development",
    "Marketing",
    "Purchasing"
]

class Person:
    def __init__(self, name="Walt"):
        self._name = None
        self.name = name

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if isinstance(value, str) and 1 < len(value) <= 25:
            self._name = value.title()
        else:
            print("Name must be string between 1 and 25 characters.")

person1 = Person("Onyi")
print(person1.name)