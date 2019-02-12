# Problem ID: 955
name = input()
l = input().strip().split(' ')
a, b, c = (int(i) for i in l)
print(name)
avg = (a+b+c)//3
print(avg)
