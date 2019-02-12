# Problem ID: 111, Min Steps to 1
def minStepsTo1BF(n):
    ''' Return Minimum no of steps required to reach 1 using Brute Force'''
    if n<=1:
        return 0
    bigNumber = 2147483647
    op1 = minStepsTo1BF(n-1)
    op2 = minStepsTo1BF(n//2) if n%2==0 else bigNumber
    op3 = minStepsTo1BF(n//3) if n%3==0 else bigNumber
    return 1 + min(op1, op2, op3)

def minStepsTo1Mem(n, storage):
    ''' Return Minimum no of steps required to reach 1 using Memoization'''
    if n<=1:
        return 0
    if storage[n] != -1:
        return storage[n]
    bigNumber = 2147483647
    op1 = minStepsTo1Mem(n-1, storage)
    op2 = minStepsTo1Mem(n//2, storage) if n%2==0 else bigNumber
    op3 = minStepsTo1Mem(n//3, storage) if n%3==0 else bigNumber
    storage[n] = 1 + min(op1, op2, op3)
    return storage[n]

def minStepsTo1Memoization(n):
    ''' Return Minimum no of steps required to reach 1 using Memoization'''
    storage = [-1] * (n+1) # Create a list with n+1 items
    return minStepsTo1Mem(n, storage)

def minStepsTo1DP(n):
    ''' Return Minimum no of steps required to reach 1 using using Dynamic Prog'''
    storage = [-1] * (n+1) # Create a list with n+1 items
    storage[0] = 0
    storage[1] = 0
    bigNumber = 2147483647
    for i in range(2,n+1):
        op1 = storage[i-1]
        op2 = storage[i//2] if i%2==0 else bigNumber
        op3 = storage[i//3] if i%3==0 else bigNumber
        storage[i] = 1 + min(op1, op2, op3)
    return storage[n]

# Main
from sys import setrecursionlimit
setrecursionlimit(11000)
n=int(input())
#print(minStepsTo1BF(n))
#print(minStepsTo1Memoization(n))
print(minStepsTo1DP(n))
