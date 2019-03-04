# Problem ID: , knapsack
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

def knapsackMem(weights, values, maxWeight, storage):
    ''' Return maximum value for a knapsack using Memoization'''
    i = len(weights)
    if storage[i][maxWeight] != -1:
        return storage[i][maxWeight]
    include = values[0] + knapsackMem(weights[1:], values[1:], maxWeight-weights[0], storage) if weights[0]<=maxWeight else smallNumber
    exclude = knapsackMem(weights[1:], values[1:], maxWeight, storage)
    storage[i][maxWeight] = max(include, exclude)
    return storage[i][maxWeight]

def knapsackMemoization(weights, values, maxWeight):
    ''' Return maximum value for a knapsack using Memoization'''
    m = 1+len(weights)
    n = 1+maxWeight
    # Create a storage of size m*n
    storage = [[-1 for i in range(n)] for j in range(m)]
    for i in range(0,m):
        storage[i][0] = 0
    for j in range(0,n):
        storage[0][j] = 0
    return knapsackMem(weights, values, maxWeight, storage)

def knapsackDP(weights, values, maxWeight):
    ''' Return maximum value for a knapsack using using Dynamic Prog'''
    m = 1+len(weights)
    n = 1+maxWeight
    # Create a storage of size m*n
    storage = [[-1 for i in range(n)] for j in range(m)]
    for i in range(0,m):
        storage[i][0] = 0
    for j in range(0,n):
        storage[0][j] = 0
    for i in range(1,m):
        for j in range(1,n):
            index = m-1-i
            include = values[index] + storage[i-1][j-weights[index]] if weights[index]<=j else 0
            exclude = storage[i-1][j]
            storage[i][j] = max(include, exclude)
            #print(storage[i][j], end=' ')
        #print(i, " Done")
    return storage[m-1][n-1]

# Main
from sys import setrecursionlimit
setrecursionlimit(11000)
import time
n=int(input())
weights=list(int(i) for i in input().strip().split(' '))
values=list(int(i) for i in input().strip().split(' '))
maxWeight=int(input())
startTime = time.time()
print(knapsackBF(weights, values, maxWeight))
print(knapsackMemoization(weights, values, maxWeight))
print(knapsackDP(weights, values, maxWeight))
endTime = time.time()
print(endTime - startTime)
