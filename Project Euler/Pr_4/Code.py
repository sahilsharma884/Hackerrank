# Project Euler #4: Largest palindrome product
#!/bin/python3

import sys

def ispalindrome(n):
    # To check whether a number 'n' is palindrome or not
    a = n
    rev = 0
    while(n > 0):
        remainder = n % 10
        rev = rev * 10 + remainder
        n = n // 10
    if a == rev:
        return True
    else:
        return False

def isthreedigitnumber(n):
    # To check whether it is three digit number or not
    # Range of three digit: [100,999]
    if n > 99 and n < 1000:
        return True
    else:
        return False

t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    flag = 0
    # Constraint 'N'
    if n > 101101 and n < 1000000:
    # Iterate N-1 in descending order
        for i in range(n-1,1,-1):
            # In each iteration, check whether it is palindrome or not.
            # If not, then move to next iterate value.
            if ispalindrome(i):
                # If yes, then find a three digit product number fot this palindrome number.
                # Iterate three digit value to check find every possible value.
                for j in range(100,1000):
                    # If a three digit number 'x' found, the other number 'y' can be calculate by dividing that
                    # 'x' number with palindrome value and then also check whether 'y' is three digit number or not.
                    if i%j == 0 and isthreedigitnumber(i//j):
                        # If yes, then signal the flag and break out the loop
                        flag = 1
                        break
                # To print the output when they got signaled and break this out of loop as we found
                if flag == 1:
                    print(i)
                    break
