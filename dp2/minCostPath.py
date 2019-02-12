# Problem ID: , minCostPath
bigNumber = 2147483647 # This is INT_MAX
def minCostPathBF(cost, i, j):
    ''' Return minimum cost path using Brute Force'''
    m = len(cost)
    n = len(cost[0])
    if m-1==i and n-1==j:
        return cost[i][j]
    op1=minCostPathBF(cost, i+1, j) if i+1 < m else bigNumber
    op2=minCostPathBF(cost, i, j+1) if j+1 < n else bigNumber
    op3=minCostPathBF(cost, i+1, j+1) if i+1<m and j+1<n else bigNumber
    ans = cost[i][j] + min(op1, op2, op3)
    return ans;

def minCostPathMem(cost, i, j, storage):
    ''' Return minimum cost path using Memoization'''
    if storage[i][j] != -1:
        return storage[i][j]
    m = len(cost)
    n = len(cost[0])
    if m-1==i and n-1==j:
        return cost[i][j]
    op1=minCostPathMem(cost, i+1, j, storage) if i+1 < m else bigNumber
    op2=minCostPathMem(cost, i, j+1, storage) if j+1 < n else bigNumber
    op3=minCostPathMem(cost, i+1, j+1, storage) if i+1<m and j+1<n else bigNumber
    storage[i][j] = cost[i][j] + min(op1, op2, op3)
    return storage[i][j]

def minCostPathMemoization(cost, i, j):
    ''' Return minimum cost path using Memoization'''
    m = len(cost)
    n = len(cost[0])
    # Create a storage of size m*n
    storage = [[-1 for i in range(n)] for j in range(m)]
    return minCostPathMem(cost, i, j, storage)

def minCostPathDP(cost, i, j):
    ''' Return minimum cost path using using Dynamic Prog'''
    m = len(cost)
    n = len(cost[0])
    # Create a storage of size m*n
    storage = [[-1 for i in range(n)] for j in range(m)]
    storage[0][0] = cost[0][0]
    for i in range(1,m):
        storage[i][0] = storage[i-1][0] + cost[i][0]
    for j in range(1,n):
        storage[0][j] = storage[0][j-1] + cost[0][j]
    for i in range(1,m):
        for j in range(1,n):
            storage[i][j] = min(storage[i-1][j], storage[i][j-1],
                    storage[i-1][j-1]) + cost[i][j]
    return storage[m-1][n-1]

# Main
from sys import setrecursionlimit
setrecursionlimit(11000)
m, n=(int(i) for i in input().strip().split(' '))
cost = [ [] ] * m
for i in range(m):
    cost[i]=list(int(i) for i in input().strip().split(' '))
print(minCostPathBF(cost, 0, 0))
print(minCostPathMemoization(cost, 0, 0))
print(minCostPathDP(cost, 0, 0))
