def differentNames(l):
    # Please add your code here
    pass

# Main
names=input().strip().split()
m=differentNames(names)
if m:
    for name in m:
        print(name, m[name])
else:
    print(-1)
