# Problem ID: 138, balancedBT
prime = 1000000007
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
n=int(input())
print(balancedBTDP(n))
