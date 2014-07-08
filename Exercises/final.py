#!/usr/local/bin/python3

import sys
import string

def remove_bad_chars(str):
   bad_chars = set(string.punctuation)
   s = ''.join(ch for ch in str if ch not in bad_chars)
   return s

def length_count(file):
   try:
     lc = {}
     f = open(file, 'r')
     for line in f:
       clean_line = remove_bad_chars(line)
       for word in clean_line.split():
         if (len(word) in lc):
           lc[len(word)] += 1
         else:
           lc[len(word)] = 1
     print("Length Count")
     for k in sorted(lc.keys()):
       print("{0} {1}".format(k, lc[k]))
   except IOError:
     print("Please provide a valid file")

if __name__ == "__main__":
   length_count(sys.argv[1])
