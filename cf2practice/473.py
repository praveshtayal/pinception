# Problem ID 473 sumOrProduct
n=int(input())
c=int(input())
if(c==1):
    result = 0
    for j in range(1, n+1):
      result += j
elif(c==2):
    result = 1
    for j in range(1, n+1):
      result *= j
else:
      result = -1
print(result)
