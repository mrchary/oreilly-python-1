#!/usr/local/bin/python3

small_words = ('into', 'the', 'a', 'of', 'at', 'in', 'for', 'on')
def book_title(title):
   """ Takes a string and returns a title-case string.
   all words EXCEPT for small words are made title case
   unless the string starts with a preoposition, in which
   case the word is correctly capitalized.

   >>> book_title('DIVE Into python')
   'Dive into Python'

   >>> book_title('the great gatsby')
   'The Great Gatsby'

   >>> book_title('the WORKS OF AleXANDer dumas')
   'The Works of Alexander Dumas'
   """
   new_title = ''
   for word in title.lower().split():
     if (word in small_words) and (new_title != ''):
       new_title += word+" "
     else:
       new_title += word.capitalize()+ " "
   return new_title.strip()

def _test():
   import doctest, refactory
   return doctest.testmod(refactory)

if __name__ == "__main__":
   _test()
