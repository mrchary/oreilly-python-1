#!/usr/local/bin/python3

while True:
   inp = input("Enter a value:")
   if inp == "":
      break
   try:
      i = int(inp)
      print("Dividing 10 by an integer")
      result = 10/i
      print(result)
   except (ValueError, TypeError):
      print("Your input must be an integer")
   except ZeroDivisionError:
      print("Your input must not be zero (0)")
