# Problem ID: 852, Min Steps to 1 using DP
def minStepsTo1DP(n):
    ''' Return Minimum no of steps required to reach 1 using using Dynamic Prog'''
    storage = [-1] * (n+1) # Create a list with n+1 items
    storage[0] = 0
    storage[1] = 0
    bigNumber = 2147483647
    for i in range(2,n+1):
        op1 = storage[i-1]
        op2 = storage[i//2] if i%2==0 else bigNumber
        op3 = storage[i//3] if i%3==0 else bigNumber
        storage[i] = 1 + min(op1, op2, op3)
    return storage[n]

# Main
n=int(input())
print(minStepsTo1DP(n))
