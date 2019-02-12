# Problem ID: 1541, staircase
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
n=int(input())
print(staircaseDP(n))
