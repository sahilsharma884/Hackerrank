# Project Euler #7: 10001st prime
#!/bin/python3

import sys
import math

def pre_prime():
    n = 1000000
    prime_bo = [True]*(n+1)
    p = 2

    # '0' and '1' are not prime number
    prime_bo[0] = False
    prime_bo[1] = False

    # Create empty list to store prime number
    prime_ = []

    # Iterate checking till sqrt(n) in lowerbound
    iter_n = math.floor(math.sqrt(n))

    # Use Sieve Algorithm
    while len(prime_) <= 10000:
        if prime_bo[p] != False:
            prime_.append(p)
        for i in range(p,len(prime_bo),p):
            prime_bo[i] = False
        
        p += 1

    return prime_

t = int(input().strip())
prime_ = pre_prime()
for a0 in range(t):
    n = int(input().strip())
    print(prime_[n-1])
