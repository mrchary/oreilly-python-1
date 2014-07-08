#!/usr/local/bin/python3

"""Check if a string is all upper case and ends with a period."""

uin = input("Please enter an upper-case string ending with a period: ")

if uin != uin.upper():
   print("Input is not all upper case.")
elif uin.endswith("."):
   print("Input meets both requirements.")
else:
   print("Input does not end with a period.")
