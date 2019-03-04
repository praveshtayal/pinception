# Problem ID: 470 Pattern
n = int(input())
print(1)
for i in range(1, n):
    for j in range(0, i+1):
        if(j==0 or j==i):
            print(i,end='')
        else:
            print(0,end='')
    print()
