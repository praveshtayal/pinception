# Problem ID: , minCostPath
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
m, n=(int(i) for i in input().strip().split(' '))
cost = [ [] ] * m
for i in range(m):
    cost[i]=list(int(i) for i in input().strip().split(' '))
print(minCostPathDP(cost, 0, 0))
