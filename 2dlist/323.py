def wavePrint(arr):
    rows = len(arr)
    cols = len(arr[0])
    for j in range(cols):
        if j%2==0:
            for i in range(rows):
                print(arr[i][j], end=' ')
        else:
            for i in range(rows-1,-1,-1):
                print(arr[i][j], end=' ')


#Main
l=[int(i) for i in input().strip().split(' ')]
m, n=l[0], l[1]
arr = [ [ l[(j*n)+i+2] for i in range(n)] for j in range(m)]
wavePrint(arr)
