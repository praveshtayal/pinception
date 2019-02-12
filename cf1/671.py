# Problem ID: 671 Triangle of Numbers
n = int(input())
for i in range(0, n):
    for j in range(1, n-i):
        print(' ', end='')
    for j in range(0, i+1):
        print(i+j+1, end='')
    for j in range(i, 0, -1):
        print(i+j, end='')
    print()
