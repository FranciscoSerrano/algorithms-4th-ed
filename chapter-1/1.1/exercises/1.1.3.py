'''
Write a program that takes three integer command line arguments and prints 
equal if all three are equal and not equal otherwise
'''

import sys

a = sys.argv[1]
b = sys.argv[2]
c = sys.argv[3]

if a == b and b ==c:
    print("Equal")
else:
    print("Not Equal")