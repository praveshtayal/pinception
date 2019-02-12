# Problem ID 475 Decimal to Binary
result=0
i=1
n=int(input())
while(n):
    if(n%2):
      result += i
    n //= 2
    i *= 10
print(result)
