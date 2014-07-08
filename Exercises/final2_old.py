#!/usr/local/bin/python3

import sys
import string

def print_length_count(lc):
   print("Length Count")
   for k in sorted(lc.keys()):
      print("{0} {1}".format(k, lc[k]))

def print_hist_macro_scale(lc):
#   Print y-axis for row values above 100 - increments of 20 
   hist = {}
   for k in lc.keys():
      row = int(lc[k]/20)
      # for each row consider the biggest word length in that range
      hist[row] = max(k,hist.get(row,0))
   top_row = max(hist.keys())
   for i in range(top_row, 4, -1):
      if ((i*20)/100 == int((i*20)/100)):
         vertical_scale = "{0:>5} -".format(i*20)
      else:
         vertical_scale = "       "
      print("{0}|{1}".format(vertical_scale, "***"*hist.get(i,0)))

def print_hist_micro_scale(lc):
#   Print y-axis for row values under 100 - increments of 5 
   hist = {}
   for k in lc.keys():
      row = int(lc[k]/5)
      # for each row consider the biggest word length in that range
      hist[row] = max(k,hist.get(row,0))
   top_row = max(hist.keys())
   for i in range(19, 0, -1):
      if ((i*5)/10 == int((i*5)/10)):
         vertical_scale = "{0:>5} -".format(i*5)
      else:
         vertical_scale = "       "
      print("{0}|{1}".format(vertical_scale, "***"*hist.get(i,0)))

def print_hist_bottom_bar(lc):
   l_max = max(lc.keys())
   c_max = max(lc.values())
   print("{0:>5} -+{1}".format("0", "-+-"*l_max))
   l2 = "       |"
   for i in range(1,l_max+1):
     l2 += "{0:>2} ".format(i)
   print(l2)

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
     return lc
   except IOError:
     print("Please provide a valid file")

if __name__ == "__main__":
   lc = length_count(sys.argv[1])
   print_length_count(lc)
   print("\n")
   print_hist_macro_scale(lc)
   print_hist_micro_scale(lc)
   print_hist_bottom_bar(lc)
   
