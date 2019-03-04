# Problem ID 1678, lootHouse
def lootHouse(houses):
    n = len(houses)
    value = [0] * (n+1)
    value[1] = houses[n-1]
    for i in range(2,n+1):
        value[i] = max(houses[n-i]+value[i-2], value[i-1])

    return value[n]

# Main
from sys import setrecursionlimit
setrecursionlimit(11000)
import time
n=int(input())
houses=list(int(i) for i in input().strip().split(' '))
print(lootHouse(houses))
