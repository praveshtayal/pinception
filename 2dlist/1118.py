def rowWiseSum(arr):
    rows = len(arr)
    cols = len(arr[0])
    l = [0] * rows
    for i in range(rows):
        for j in range(cols):
            l[i] += arr[i][j]
    return l

#Main
m, n=(int(i) for i in input().strip().split(' '))
l=[int(i) for i in input().strip().split(' ')]
arr = [ [ l[(j*n)+i] for i in range(n)] for j in range(m)]
l=rowWiseSum(arr)
print(*l)
