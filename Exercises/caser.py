#!/usr/local/bin/python3

import sys

def capitalize(str):
    return str.capitalize()

def title(str):
    return str.title()

def upper(str):
    return str.upper()

def lower(str):
    return str.lower()

def exit(str):
    print("Goodbye for now!")
    sys.exit()

switch = {
	'capitalize':capitalize,
	'title':title,
	'upper':upper,
	'lower':lower,
	'exit':exit
	}

while True:
   inp1 = input('Enter a function name (capitalize, title, upper, lower or exit):')
   inp2 = input('Enter a string:')

   option = switch.get(inp1, None)
   if option:
      res = option(inp2)
      print(res)
   else:
      print("'"+inp1+"' is not a valid function")
