#!/usr/local/bin/python3
"""Detect any mention of Python in the user's input."""

uin = input("Please enter a sentence: ")
if "python" in uin.lower():
  print("Ah Ha! You mentioned Python.")
elif "perl" in uin.lower():
  print("OMG! You mentioned Perl.")
elif "ruby" in uin.lower():
  print("So Sweet :) You mentioned Ruby.")
else:
  print("Didn't see any languages there.")

