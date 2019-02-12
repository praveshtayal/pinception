# Problem ID: 467 Find power of a number
l = input().strip().split(' ')
base, n = (int(i) for i in l)
result = 1
for i in range(0,n):
    result *= base
print(result)
