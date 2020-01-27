# Project Euler #6: Sum square difference
#!/bin/python3

import sys

def sum_natural(N):
    return int(N*(N+1)/2)

def square_sum_natural(N):
    return int(N*(N+1)*(2*N+1)/6)

t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    
    print(sum_natural(n)**2 - square_sum_natural(n))
