# Problem ID: 1676, knapsack
smallNumber = -2147483648 # This is INT_MIN
def knapsackBF(weights, values, maxWeight):
    ''' Return maximum value for a knapsack using Brute Force'''
    n = len(weights)
    if n==0:
        return 0
    include = values[0] + knapsackBF(weights[1:], values[1:],
            maxWeight-weights[0]) if weights[0]<=maxWeight else smallNumber
    exclude = knapsackBF(weights[1:], values[1:], maxWeight)
    ans = max(include, exclude)
    return ans;

# Main
from sys import setrecursionlimit
setrecursionlimit(11000)
n=int(input())
weights=list(int(i) for i in input().strip().split(' '))
values=list(int(i) for i in input().strip().split(' '))
maxWeight=int(input())
print(knapsackBF(weights, values, maxWeight))
