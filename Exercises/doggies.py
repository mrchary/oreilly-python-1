#!/usr/local/bin/python3
"""Sn00p Doggie Doggin'"""

class Dog:
   def __init__(self, name, breed):
      global dogs
      self.name = name
      self.breed = breed

if __name__ == "__main__":
   dogs = []
   while True:
      name = input("Name: ")
      if (name == ""):
         break
      breed = input("Breed: ")
      dog = Dog(name, breed)
      dogs.append(dog)
      print("DOGS")
      for i, dog in enumerate(dogs):
        print("{0}. {1}:{2}".format(i, dog.name, dog.breed))
