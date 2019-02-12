# Problem ID: , lcs
def lcsBF(s1, s2):
    ''' Return lcs using Brute Force'''
    m = len(s1)
    n = len(s2)
    if m==0 or n==0:
        return 0
    if s1[0] == s2[0]:
        return 1+lcsBF(s1[1:], s2[1:])
    op1 = lcsBF(s1[1:], s2)
    op2 = lcsBF(s1, s2[1:])
    ans = max(op1, op2)
    return ans;

def lcsMem(s1, s2, storage):
    ''' Return lcs using Memoization'''
    m = len(s1)
    n = len(s2)
    if storage[m][n] != -1:
        return storage[m][n]
    if s1[0] == s2[0]:
        return 1+lcsMem(s1[1:], s2[1:], storage)
    op1 = lcsMem(s1[1:], s2, storage)
    op2 = lcsMem(s1, s2[1:], storage)
    storage[m][n] = max(op1, op2)
    return storage[m][n]

def lcsMemoization(s1, s2):
    ''' Return lcs using Memoization'''
    m = len(s1)
    n = len(s2)
    # Create a storage of size m+1*n+1
    storage = [[-1 for i in range(n+1)] for j in range(m+1)]
    for i in range(0,m+1):
        storage[i][0] = 0
    for j in range(0,n+1):
        storage[0][j] = 0
    return lcsMem(s1, s2, storage)

def lcsDP(s1, s2):
    ''' Return lcs using using Dynamic Prog'''
    m = len(s1)
    n = len(s2)
    # Create a storage of size m+1*n+1
    storage = [[-1 for i in range(n+1)] for j in range(m+1)]
    for i in range(0,m+1):
        storage[i][0] = 0
    for j in range(0,n+1):
        storage[0][j] = 0
    for i in range(1,m+1):
        for j in range(1,n+1):
            if s1[m-i] == s2[n-j]:
                storage[i][j] = 1+storage[i-1][j-1]
            else:
                storage[i][j] = max(storage[i-1][j], storage[i][j-1])
    return storage[m][n]

# Main
from sys import setrecursionlimit
setrecursionlimit(11000)
s1 =input().strip()
s2 =input().strip()
print(lcsBF(s1, s2))
#print(lcsMemoization(s1, s2))
print(lcsDP(s1, s2))
