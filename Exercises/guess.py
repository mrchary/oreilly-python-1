#!/usr/local/bin/python3

secret = 6
try_count = 0 

while True:
  try_count += 1
  if (try_count == 6):
      print("Sorry, the number was ",secret)
      break
  number = int(input("Guess a number: "))
  if (number < secret):
      print("Guess higher")
  elif (number > secret):
      print("Guess lower")
  else:
      print("Correct! Well done, the number was ",secret)
      break 
  
