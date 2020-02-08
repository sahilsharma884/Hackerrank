# Project Euler #8: Largest product in a series
#!/bin/python3

import sys

# Number of test case
t = int(input().strip())
for a0 in range(t):
    # n: Number of digits
    # k: number of windows size
    n,k = input().strip().split(' ')
    n,k = [int(n),int(k)]
    num = input().strip()
    # Convert them into list
    num = list(map(int,list(str(num))))
    # Find the length of the number
    len_num = len(num)
    # Initialize variable for starting point
    i = 0
    # Initialize porduct max value is -1
    max_ = -1
    # Checking starting point and end point are within the list
    while (i+k) <= len_num:
      prod_ = 1
      # Fetch the list of elements inside the windows size and product all of them within the size of windows size
      for m in num[i:i+k]:
        prod_ *= m
      # If existing one is smaller than the latest one we got above, update it
      if max_ < prod_:
        max_ = prod_
      # Increment the next starting point
      i += 1
    # Display the output of the result
    print(max_)
