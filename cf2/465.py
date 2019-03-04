# Problem ID 465 Binary to decimal
result=0
i=1
n=int(input())
while(n):
    if(n%10):
      result += i
    n //= 10
    i *= 2
print(result)
