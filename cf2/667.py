# Problem ID 667 Number Pattern
n=int(input())
for i in range(n, 0, -1):
    k=i
    for j in range(1,n+1):
        print(k, end='')
        if(k<n):
            k+=1
    print()
