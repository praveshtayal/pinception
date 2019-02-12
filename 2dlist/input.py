#Main
m, n=(int(i) for i in input().strip().split(' '))
# List in m lines
arr = [ [] ] * m
for i in range(m):
    arr[i]=list(int(i) for i in input().strip().split(' '))
# List in one lines
l=[int(i) for i in input().strip().split(' ')]
arr = [ [ l[(j*n)+i] for i in range(n)] for j in range(m)]
