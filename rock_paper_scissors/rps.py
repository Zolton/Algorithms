#!/usr/bin/python

import sys

def rock_paper_scissors(n):
  # possible = ["rock", "paper", "scissors"]
  # count = 0
  # solution = []
  # if count >= n:
  #   rock_paper_scissors
  # else:
  #   count = count + 1
  #   for 
  # for i in range(len(possible)):
  #   for j in possible:
  #     print([possible[j]])
      #print(i)
      #print(j)


print(rock_paper_scissors(2))


if __name__ == "__main__":
  if len(sys.argv) > 1:
    num_plays = int(sys.argv[1])
    print(rock_paper_scissors(num_plays))
  else:
    print('Usage: rps.py [num_plays]')