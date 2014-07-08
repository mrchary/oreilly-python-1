#!/usr/local/bin/python3

out = ''
reversed_out = ''
inp = input('Message:')

for i in range(len(inp)):
  out += chr(ord(inp[i])+1)
lst_rev_out = reversed(out)

for i in lst_rev_out:
  reversed_out += i

print(reversed_out)
