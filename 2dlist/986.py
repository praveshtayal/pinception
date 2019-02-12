def largestRowCol(arr):
    rows = len(arr)
    cols = len(arr[0])
    sumRow = [0] * rows
    sumCol = [0] * cols
    for i in range(rows):
        for j in range(cols):
            sumRow[i] += arr[i][j]
            sumCol[j] += arr[i][j]

    # Assume row 0 has maximum sum
    l = ['row', 0, sumRow[0]]
    for i in range(rows):
        if sumRow[i] > l[2]:
            l[2] = sumRow[i]
            l[1] = i
    for j in range(cols):
        if sumCol[j] > l[2]:
            l[2] = sumCol[j]
            l[1] = j
            l[0] = 'column'
    return l

#Main
m, n=(int(i) for i in input().strip().split(' '))
l=[int(i) for i in input().strip().split(' ')]
arr = [ [ l[(j*n)+i] for i in range(n)] for j in range(m)]
l=largestRowCol(arr)
print(*l)
