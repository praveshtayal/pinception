# Problem ID 1101 Array Sum
n=int(input())
arr=list(int(i) for i in input().strip().split(' '))
result = 0
for number in arr:
    result += number
print(result)
