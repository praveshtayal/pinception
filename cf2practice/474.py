# Problem ID 474 Terms of AP
n=int(input())
j=1
k=1
while(k<=n):
    result = 3*j + 2
    j += 1
    if(result%4==0):
      continue
    print(result, end=' ')
    k += 1
