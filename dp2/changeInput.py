t = tuple(int(i) for i in input().strip().split(' '))
m = t[0]
n = t[1]
print(m, n)
index=2
for i in range(0,m):
    for j in range(0,n):
        print(t[index+j], end=' ')
    print()
    index += n
