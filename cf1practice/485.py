# Problem ID: 485 Find average Marks Best 2
name = input().strip()[0]
l = input().strip().split(' ')
a, b, c = (int(i) for i in l)
if (a<b and a<c):
    sum = b+c
elif (b<a and b<c):
    sum = a+c
else:
    sum = a+b
print(name, sum//2, sep=' ')
