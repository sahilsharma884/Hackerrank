# Project Euler #2: Even Fibonacci numbers
#!/bin/python3

import sys


t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    a = 1
    b = 2
    sum1 = 2
    c = a + b
    while(c < n):
        if (c % 2 == 0):
            sum1 += c
        a = b
        b = c
        c = a + b
    
    print(sum1)
