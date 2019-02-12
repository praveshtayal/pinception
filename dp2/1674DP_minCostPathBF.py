# Problem ID: 1674, minCostPath
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

# Main
from sys import setrecursionlimit
setrecursionlimit(11000)
m, n=(int(i) for i in input().strip().split(' '))
cost = [ [] ] * m
for i in range(m):
    cost[i]=list(int(i) for i in input().strip().split(' '))
print(minCostPathBF(cost, 0, 0))
