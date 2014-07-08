#!/usr/local/bin/python3

lower_words = []
upper_words = []

s = input("Input your text:")

words = s.strip().split()

for word in words:
  if word == word.lower():
    lower_words.append(word)
  else:
    upper_words.append(word)

for upper_then_lower_word in upper_words+lower_words:
  print(upper_then_lower_word)
