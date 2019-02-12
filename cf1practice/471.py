# Problem ID: 472
n = int(input())
for i in range(0, n):
    for j in range(0, i+1):
        if(j==0 or j==i):
            print(1,end='')
        else:
            print(2,end='')
    print()
