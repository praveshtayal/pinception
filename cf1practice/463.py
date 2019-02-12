# Problem ID: 463
c = input()[0]
if ('a'<= c and c <= 'z'):
    out = 0
elif ('A'<= c and c <= 'Z'):
    out = 1
else:
    out = -1
print(out)
