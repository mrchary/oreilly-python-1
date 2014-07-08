#!/usr/local/bin/python3

word_set = set()
word_dict = {}

while True:
  s = input("Enter text: ")
  if not s:
    print("Finished")
    break
  else:
    for punc in ",?;.":
      s = s.replace(punc, " ")
    words = s.lower().split()
    for word in words:
      previous_size = len(word_set)
      word_set.add(word)
      if (previous_size < len(word_set)):
        word_dict[word] = len(word_set)
    for word in word_dict.keys():
      print(word, " : ", word_dict[word]) 
