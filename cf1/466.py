# Problem ID: 466 Sum of even & odd
n = int(input())
odd = even = 0
while(n):
    digit = n%10
    n = n//10
    if(digit%2==0):
        even += digit
    else:
        odd += digit
print(even, odd, sep=' ')
