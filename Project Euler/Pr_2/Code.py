# Project Euler #2: Even Fibonacci numbers
#!/bin/python3

import sys


t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    # Initialize first and second value to generate Fibonacci's series
    a = 1
    b = 2
    # Since initializing two number, one of them is even (b=2).
    # So, we initialize with starting sum_ as 2
    sum1 = 2
    # Fibonacci's series works as take previous two input and put into third variable
    c = a + b
    # Generate fibonacci's series until less than 'n'
    while(c < n):
        # If third variable is even, then add them. That's our task.
        # Task: Add those number which are even
        if (c % 2 == 0):
            sum1 += c
        # The next three line is that how Fibonacci's series works
        a = b
        b = c
        c = a + b
    # Generate output of sum_
    print(sum1)
