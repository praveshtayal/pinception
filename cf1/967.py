# Problem ID: 967 Number Pattern 1
n = int(input())
for i in range(0, n):
    for j in range(0, i+1):
        print(i+j+1, end='')
    print()
