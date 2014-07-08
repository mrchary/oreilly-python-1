#!/usr/local/bin/python3
""" Demonstrates the need for caching """

def kid(a, b):
   """ Multiplication the hard way """
   c = 0
   for i in range(b):
      c += a
   return c

while True:
  a = input('enter a number: ')
  b = input('enter another number: ')
  a = int(a)
  b = int(b)
  print(kid(a,b))
