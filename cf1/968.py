# Problem ID: 968
n = int(input())
for i in range(0, n):
    for j in range(1, n-i):
        print(' ', end='')
    for j in range(0, i+1):
        print(i+j+1, end='')
    print()
