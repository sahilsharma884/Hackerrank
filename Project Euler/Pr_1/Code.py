# Project Euler #1: Multiples of 3 and 5
#!/bin/python3

import sys

# Define sum of natural number formula
def sumNatural(n):
    return (n*(n+1))//2

test_case = int(input().strip())
for i in range(test_case):
    n = int(input().strip())
    
    # To find N3
    # If n is divisible by 3, we divide by 3 and take lower roundoff value and explicity subtract 1
    if n%3 == 0:
        n_3 = ((n//3)-1)
    # Otherwise simply divide by 3 and take lower roundoff value
    else:
        n_3 = (n//3)
        
    # To find N5
    # If n is divisible by 5, we divide by 5 and take lower roundoff value and explicity subtract 1
    if n%5 == 0:
        n_5 = ((n//5)-1)
    # Otherwise simply divide by 5 and take lower roundoff value    
    else:
        n_5 = (n//5)
    
    # To find N15
    # If n is divisible by 15, we divide by 15 and take lower roundoff value and explicity subtract 1
    if n%15 == 0:
        n_15 = ((n//15)-1)
    # Otherwise simply divide by 15 and take lower roundoff value
    else:
        n_15 = (n//15)
    
    # We apply formula of sum of natural number with parameter which contain number of sets(N3;N5;N15)
    r = sumNatural(n_3)*3 + sumNatural(n_5)*5 - sumNatural(n_15)*15
    
    # Generate output of result
    print(r)
