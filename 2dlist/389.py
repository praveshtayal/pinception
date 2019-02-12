def spiralPrint(arr):
    rows = len(arr)
    cols = len(arr[0])
    startRow, startCol, endRow, endCol = 0, 0, rows-1, cols-1
    while startRow<=endRow and startCol<=endCol:
        # Print startRow
        for j in range(startCol, endCol+1):
            print(arr[startRow][j], end=' ')
        startRow += 1
        if startRow>endRow or startCol>endCol:
            break

        # Print endCol
        for i in range(startRow, endRow+1):
            print(arr[i][endCol], end=' ')
        endCol -= 1
        if startRow>endRow or startCol>endCol:
            break

        # Print endRow
        for j in range(endCol, startCol-1, -1):
            print(arr[endRow][j], end=' ')
        endRow -= 1
        if startRow>endRow or startCol>endCol:
            break

        # Print startCol
        for i in range(endRow, startRow-1, -1):
            print(arr[i][startCol], end=' ')
        startCol += 1


#Main
l=[int(i) for i in input().strip().split(' ')]
m, n=l[0], l[1]
arr = [ [ l[(j*n)+i+2] for i in range(n)] for j in range(m)]
spiralPrint(arr)
