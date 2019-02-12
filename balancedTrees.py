def balancedTrees(limit):
    n = 1000
    l = [0] * n    # list l has n elements
    l[1] = 1       # balanced trees of ht 1 are 1
    for h in range(2,n):
        l[h] = (2 * l[h-1] * l[h-2])   +   (l[h-1] * l[h-1])
        print(h, l[h])
        if l[h]>limit:
            return l
    return l

balancedTrees(10**1000000)
