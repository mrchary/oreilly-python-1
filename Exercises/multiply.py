#!/usr/local/bin/python3

data = ((1,1),(22,56),(30,4),(4,4),(99,99))

for tuple in data:
  print("{0:>4d} = {1:>2d} x {2:>2d}".format(tuple[0]*tuple[1],tuple[0],tuple[1]))
