# Project Euler #3: Largest prime factor
#!/bin/python3

import sys
import math

def isprime(number):
    if number == 2 or number == 3:
        return True
    else:
        flag = 0
        for i in range(2,math.floor(math.sqrt(number))+1):
            if number % i == 0:
                flag = 1
                break
    if flag == 1:
        return False
    else:
        return True

t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    max_ = 0
    if isprime(n):
        max_ = n
    else:
        for i in range(2,math.floor(math.sqrt(n))+1):
            if n % i == 0:
                if isprime(i):
                    max_ = i
                if isprime(n//i) and max_ < n//i:
                    max_ = n//i
    print(max_)
