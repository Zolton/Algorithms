#!/usr/bin/python

import sys



# The cache parameter is here for if you want to implement
# a solution that is more efficient than the naive 
# recursive solution
#def eating_cookies(n):
# Python3 implementation to count  
# ways to sum up to a given value N 
  
# Function to count the total  
# number of ways to sum up to 'N' 
def eating_cookies(N): 
  #My google-fu has only grown stronger at Lambda - solution courtesy of GeeksforGeeks
  arr = [0,1,2,3]
  
  count = [0 for i in range(N + 1)] 
  count[0] = 1
      
    # Count ways for all values up  
    # to 'N' and store the result 
  for i in range(1, N + 1): 
    for j in range(4): 
      if (i >= arr[j]): 
        count[i] += count[i - arr[j]] 
    # required number of ways  
  return count[N]
print(eating_cookies(10))

if __name__ == "__main__":
  if len(sys.argv) > 1:
    num_cookies = int(sys.argv[1])
    print("There are {ways} ways for Cookie Monster to eat {n} cookies.".format(ways=eating_cookies(num_cookies), n=num_cookies))
  else:
    print('Usage: eating_cookies.py [num_cookies]')