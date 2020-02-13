# Project Euler #9: Special Pythagorean triplet
#!/bin/python3

import sys
import math

def pythagoras(a,b,c):
    if a**2 + b**2 == c**2:
        return True
    else:
        return False


t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    max_prod = -1
    for a in range(1,math.floor(n/2)):
        b = int(((n*n) - (2*n*a)) / ((2*n) - (2*a)))
        c = n-a-b
        if max_prod < a*b*c and a < b and b < c and a < c  and pythagoras(a,b,c):
            max_prod = a*b*c
    print(max_prod)
