def findMaxSquareWithAllZeros(arr):
    #  Given a n*m matrix which contains only 0s and 1s, find out the size of
    #  maximum square sub-matrix with all 0s. You need to return the size of
    #  square with all 0s. */
    row = len(arr)
    col = len(arr[0])
    # Create a storage of size row+1*col+1
    storage = [[0 for i in range(col+1)] for j in range(row+1)]
    for i in range(row-1,-1,-1):
        for j in range(col-1,-1,-1):
            storage[i][j] = max(storage[i+1][j], storage[i][j+1])
            maximum = storage[i][j]

            if min(row-i, col-j)<=maximum:
                continue

            foundOne = False
            for p in range(0, maximum+1):
                for q in range(0, maximum+1):
                    if arr[i+p][j+q]==1:
                        foundOne = True
                        break
                if foundOne:
                    break
            if foundOne==False:
                storage[i][j] += 1
    return storage[0][0]

# Main
m, n=(int(i) for i in input().strip().split(' '))
mat = [ [] ] * m
for i in range(m):
    mat[i]=list(int(i) for i in input().strip().split(' '))
print(findMaxSquareWithAllZeros(mat))
