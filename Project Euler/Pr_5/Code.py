#!/bin/python3

import sys
import math

# Multply key value that number of 'val' occurs
def multiply(pn,val):
    m = 1
    for i in range(val):
        m *= pn
        
    return m

# create list of prime of prime number with counter
def pf_dict(num):
    temp_ = {}
    i = 2
    while num!= 1:
        if num%i == 0:
            num = int(num/i)
            if i in temp_:
                temp_[i] = temp_.get(i) + 1
            else:
                temp_[i] = 1
        else:
            i = i+1
        
    return temp_
            

def isprime(num):
    flag = 0
    # Intialling 1,2 consider prime number
    if num <= 2:
        return True
    # Checking whether number is prime or not
    # Iterating from 2 to lowerbound(sqrt(num))
    for i in range(2,math.floor(math.sqrt(num))+1):
        # If any number divisible by i, that means its not prime number
        if num%i == 0:
            flag = 1
            break
    # If its found that it is not prime number, we create a list of factor for that number
    if flag == 1:
        return False
    else:
    # If it is prime, then return prime number
        return True

t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    # Initialize product result = 1
    prod_ = 1
    # Create dictionary to store prime number as key and occurs of factor of each number as value
    # Read the algorithm in README.md
    pr_ = {}
    for i in range(1,n+1):
        # If it is prime number, just multiply it by prime number
        if isprime(i):
            pr_[i] = 1
            prod_ *= i
        # If not then
        else:
            # Generate the dict contain factors of non-prime number
            # For example: if i=4, which is non-prime number
            # it will return: {2:2} (that because, 4=2x2 so, key is prime number (2) and value is occurence of that prime number)
            # since 2 comes two times so, 2)
            # Similarily, another example: if i=10, then it will return: {2:1,5:1} (as 10=2*5, here keys are 2 and 5 and 
            # values are occurrence of each prime number that is 2 occur 1 time and 5 occur 1 time)
            r_dict = pf_dict(i)
            # Rest are as follows as per algorithm
            for pn,val in r_dict.items():
                if pr_.get(pn) >= val:
                    r_dict[pn] = 0
                    continue
                else:
                    r_dict[pn] = r_dict[pn] - pr_.get(pn)

            for pn,val in r_dict.items():
                m = multiply(pn,val)
                prod_ *= m
            
            # Update prime number of product result updates for further number.
            for pn,val in r_dict.items():
                pr_[pn] = pr_.get(pn) + val                
            
    print(prod_)
