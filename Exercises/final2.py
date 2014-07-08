#!/usr/local/bin/python3

import sys
import string

def print_length_count(lc):
   print("Length Count")
   for k in sorted(lc.keys()):
      print("{0} {1}".format(k, lc[k]))

def remove_bad_chars(str):
   bad_chars = set(string.punctuation)
   s = ''.join(ch for ch in str if ch not in bad_chars)
   return s

def build_histogram_matrix(lc):
   matrix = {}
   for x in lc.keys():
      if (lc[x] > 99):
         for y in range(100, int(lc[x]/20)*20+20, 20):
            matrix[(x,y)] = 1
      for y in range(0, min(100,int(lc[x]/5)*5)+5, 5):
         matrix[(x,y)] = 1
   return matrix

def print_histogram(matrix,lc):
   max_count = max(lc.values())
   max_length = max(lc.keys())

   # print large scale
   if (max_count > 99):
     for y in range(int(max_count/20)*20, 80, -20): 
        if (y/100 == int(y/100)):
           y_scale = "{0:>5} -".format(y)
        else:
           y_scale = "       "
        row = ""
        for x in range(1, max_length+1, 1):
           if (matrix.get((x,y),0)):
             row += "***"
           else:
             row += "   "
        print("{0}|{1}".format(y_scale, row))
  
   # print small scale
   for y in range(min(95,int(max_count/5)*5), 0, -5): 
     if (y/10 == int(y/10)):
       y_scale = "{0:>5} -".format(y)
     else:
       y_scale = "       "
     row = ""
     for x in range(1, max_length+1, 1):
       if (matrix.get((x,y),0)):
         row += "***"
       else:
         row += "   "
     print("{0}|{1}".format(y_scale, row))

   # print bottom bar 
   print("{0:>5} -+{1}".format("0", "-+-"*max_length))
   x_scale = "       |"
   for i in range(1,max_length+1):
     x_scale += "{0:>2} ".format(i)
   print(x_scale)

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
     return lc
   except IOError:
     print("Please provide a valid file")

if __name__ == "__main__":
   lc = length_count(sys.argv[1])
   matrix = build_histogram_matrix(lc)
   print_length_count(lc)
   print("\n")
   print_histogram(matrix,lc)
