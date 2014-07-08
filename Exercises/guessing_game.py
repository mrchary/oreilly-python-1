#!/usr/local/bin/python3

import random

target_number = random.randrange(1,100)

while True:
   inp = int(input("guess a number: "))
   if inp == target_number:
      print("You guessed it!")
      break
   elif inp < target_number:
      print("Too low")
   else:
      print("Too high")      
