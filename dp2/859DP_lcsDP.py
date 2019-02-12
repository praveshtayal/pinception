# Problem ID: 859, lcs
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
s1 =input().strip()
s2 =input().strip()
print(lcsDP(s1, s2))
