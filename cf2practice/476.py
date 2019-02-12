# Problem ID 476 Square Root (Integral)
n=int(input())
for j in range(1, n+1):
    result = j*j
    if(result==n):
        print(j)
        break
    elif(result>n):
        print(j-1)
        break
