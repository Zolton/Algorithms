#!/usr/bin/python

import argparse
arr = [10, 7, 5, 8, 11, 9]
def find_max_profit(prices):
  profit = []
  for i in range(len(prices)):
    #print("This is i: ", prices[i])
    for j in range(i+1, len(prices)):
      buy = prices[i]
      future = prices[j]
      currentP = future - buy
      # print("This is i: ", prices[i])
      # print("This is j: ", prices[j])
      # print("this is current: ", currentP)
      profit.append(currentP)
  return max(profit)

print("Max profit is: ", find_max_profit(arr))

if __name__ == '__main__':
  # This is just some code to accept inputs from the command line
  parser = argparse.ArgumentParser(description='Find max profit from prices.')
  parser.add_argument('integers', metavar='N', type=int, nargs='+', help='an integer price')
  args = parser.parse_args()

  print("A profit of ${profit} can be made from the stock prices {prices}.".format(profit=find_max_profit(args.integers), prices=args.integers))