# Problem ID: , editDistance
def editDistanceBF(s1, s2):
    ''' Return editDistance using Brute Force'''
    m = len(s1)
    n = len(s2)
    if m==0:
        return n
    if n==0:
        return m
    if s1[0] == s2[0]:
        return editDistanceBF(s1[1:], s2[1:])
    op1 = editDistanceBF(s1[1:], s2)
    op2 = editDistanceBF(s1, s2[1:])
    op3 = editDistanceBF(s1[1:], s2[1:])
    ans = 1+min(op1, op2, op3)
    return ans;

def editDistanceMem(s1, s2, storage):
    ''' Return editDistance using Memoization'''
    m = len(s1)
    n = len(s2)
    if storage[m][n] != -1:
        return storage[m][n]
    if s1[0] == s2[0]:
        return editDistanceMem(s1[1:], s2[1:], storage)
    op1 = editDistanceMem(s1[1:], s2, storage)
    op2 = editDistanceMem(s1, s2[1:], storage)
    op3 = editDistanceMem(s1[1:], s2[1:], storage)
    storage[m][n] = 1+min(op1, op2, op3)
    return storage[m][n]

def editDistanceMemoization(s1, s2):
    ''' Return editDistance using Memoization'''
    m = len(s1)
    n = len(s2)
    # Create a storage of size m+1*n+1
    storage = [[-1 for i in range(n+1)] for j in range(m+1)]
    for i in range(0,m+1):
        storage[i][0] = 0
    for j in range(0,n+1):
        storage[0][j] = 0
    return editDistanceMem(s1, s2, storage)

def editDistanceDP(s1, s2):
    ''' Return editDistance using using Dynamic Prog'''
    m = len(s1)
    n = len(s2)
    # Create a storage of size m+1*n+1
    storage = [[-1 for i in range(n+1)] for j in range(m+1)]
    storage[0][0] = 0
    for i in range(1,m+1):
        storage[i][0] = i
    for j in range(1,n+1):
        storage[0][j] = j
    for i in range(1,m+1):
        for j in range(1,n+1):
            if s1[m-i] == s2[n-j]:
                storage[i][j] = storage[i-1][j-1]
            else:
                storage[i][j] = 1+min(storage[i-1][j], storage[i][j-1],
                        storage[i-1][j-1])
    return storage[m][n]

# Main
from sys import setrecursionlimit
setrecursionlimit(11000)
s1 =input().strip()
s2 =input().strip()
print(editDistanceBF(s1, s2))
#print(editDistanceMemoization(s1, s2))
print(editDistanceDP(s1, s2))
