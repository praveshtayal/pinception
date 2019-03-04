# Problem ID 468 Reverse of a number
result=0
n=int(input())
while(n):
    digit = n%10
    n //= 10
    result = result*10 + digit
print(result)
