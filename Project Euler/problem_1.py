#!/bin/python3

import sys


def sumNatural(n):
    return (n*(n+1))//2

test_case = int(input().strip())
for i in range(test_case):
    n = int(input().strip())
    if n%3 == 0:
        n_3 = ((n//3)-1)
    else:
        n_3 = (n//3)
        
    if n%5 == 0:
        n_5 = ((n//5)-1)
    else:
        n_5 = (n//5)
        
    if n%15 == 0:
        n_15 = ((n//15)-1)
    else:
        n_15 = (n//15)
    
    r = sumNatural(n_3)*3 + sumNatural(n_5)*5 - sumNatural(n_15)*15
    print(r)
