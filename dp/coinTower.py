# Problem ID: , coinTower
def coinTowerDP(n, x, y):
    # Create a storage of size n+1
    # True represent Player having option i will win
    # False represent Player having option i will loose
    storage = [False] * (n+1)
    storage[0] = True
    storage[1] = True # We can always remove 1 coin
    storage[x] = True
    storage[y] = True
    for i in range(2,n+1):
        if not storage[i]:
            for option in (i-1, i-x, i-y):
                if storage[option-1]==False and (
                   option-x not in range(0,n) or storage[option-x]==False) and (
                   option-y not in range(0,n) or storage[option-y]==False):
                    storage[i] = True
                    break
    return storage[n]

# Main
n,x,y=(int(i) for i in input().strip().split(' '))
print('Beerus') if coinTowerDP(n, x, y) else print('Whis')
