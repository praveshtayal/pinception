# Problem ID: 1541, balancedBT
prime = 1000000007
def balancedBTBF(n):
    ''' Return no of balanced BT of height n using Brute Force'''
    if n<=1:
        return 1
    n1 = balancedBTBF(n-1)
    n2 = balancedBTBF(n-2)
    ans = (((n1*n1)%prime) + ((2*n1*n2)%prime)) % prime
    return ans;

def balancedBTMem(n, storage):
    ''' Return no of balanced BT of height n using Memoization'''
    if storage[n] != -1:
        return storage[n]
    n1 = balancedBTMem(n-1, storage)
    n2 = balancedBTMem(n-2, storage)
    storage[n] = (((n1*n1)%prime) + ((2*n1*n2)%prime)) % prime
    return storage[n]

def balancedBTMemoization(n):
    ''' Return no of balanced BT of height n using Memoization'''
    storage = [-1] * max(2, n+1) # Create a list with n+1 items
    storage[0] = 1
    storage[1] = 1
    return balancedBTMem(n, storage)

def balancedBTDP(n):
    ''' Return no of balanced BT of height n using using Dynamic Prog'''
    storage = [-1] * max(2, n+1) # Create a list with n+1 items
    storage[0] = 1
    storage[1] = 1
    for i in range(2,n+1):
        n1 = storage[i-1]
        n2 = storage[i-2]
        storage[i] = (((n1*n1)%prime) + ((2*n1*n2)%prime)) % prime
    return storage[n]

# Main
from sys import setrecursionlimit
setrecursionlimit(11000)
n=int(input())
print(balancedBTBF(n))
print(balancedBTMemoization(n))
print(balancedBTDP(n))
