def freqMap(l):
    map = {}
    for num in l:
        if num in map:
            map[num] += 1
        else:
            map[num] = 1
    return map

def differentNames(l):
    m = freqMap(l)
    ans = {}
    for name in m:
        if m[name]!=1:
            ans[name] = m[name]
    return ans

# Main
names=input().strip().split()
m=differentNames(names)
if m:
    for name in m:
        print(name, m[name])
else:
    print(-1)
