#!/usr/local/bin/python3

text_file = open('text_file.txt','a')
text_file.close()

while True:
  text_file = open('text_file.txt','r')
  for line in text_file:
    print(line)
  text_file.close()

  inp = input('Enter text:')
 
  if inp == '':
    break

  text_file = open('text_file.txt','a')
  text_file.write(inp)
  text_file.close()
