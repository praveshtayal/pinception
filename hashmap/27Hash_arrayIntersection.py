# Problem ID 27: print Array Intersection 
def freqMap(l):
    map = {}
    for num in l:
        if num in map:
            map[num] += 1
        else:
            map[num] = 1
    return map

def arrayIntersection(l1, l2):
    map1 = freqMap(l1)
    map2 = freqMap(l2)
    l3 = []
    for num in map1:
        if num in map2:
            l = [num] * min(map1[num], map2[num])
            l3.extend(l)
    return l3

# Main
n=int(input())
l1=list(int(i) for i in input().strip().split(' '))
n=int(input())
l2=list(int(i) for i in input().strip().split(' '))
l3 = arrayIntersection(l1, l2)
for num in l3:
    print(num)
