# Problem ID: 1541, staircase
def staircaseBF(n):
    ''' Return possible no of ways to climb n staircase using Brute Force'''
    if n<=0:
        return 0
    if n==1 or n==2:
        return n
    if n==3:
        return 4
    return staircaseBF(n-1) + staircaseBF(n-2) + staircaseBF(n-3)

def staircaseMem(n, storage):
    ''' Return possible no of ways to climb n staircase using Memoization'''
    if storage[n] != -1:
        return storage[n]
    storage[n] = staircaseMem(n-1, storage) + staircaseMem(n-2,
            storage) + staircaseMem(n-3, storage)
    return storage[n]

def staircaseMemoization(n):
    ''' Return possible no of ways to climb n staircase using Memoization'''
    storage = [-1] * max(4, n+1) # Create a list with n+1 items
    storage[0] = 0
    storage[1] = 1
    storage[2] = 2
    storage[3] = 4
    return staircaseMem(n, storage)

def staircaseDP(n):
    ''' Return possible no of ways to climb n staircase using using Dynamic Prog'''
    storage = [-1] * max(4, n+1) # Create a list with n+1 items
    storage[0] = 0
    storage[1] = 1
    storage[2] = 2
    storage[3] = 4
    for i in range(4,n+1):
        storage[i] = storage[i-1] + storage[i-2] + storage[i-3]
    return storage[n]

# Main
from sys import setrecursionlimit
setrecursionlimit(11000)
n=int(input())
print(staircaseBF(n))
print(staircaseMemoization(n))
print(staircaseDP(n))
