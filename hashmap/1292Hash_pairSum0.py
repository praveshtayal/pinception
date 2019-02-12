# Problem ID 1292: pairSum to 0
def freqMap(l):
    map = {}
    for num in l:
        if num in map:
            map[num] += 1
        else:
            map[num] = 1
    return map

def pairSum0(l):
    m = freqMap(l)
    for num in m:
        if num>=0 and -num in m:
            for _ in range(0, m[num]*m[-num]):
                print(-num, num)

# Main
n=int(input())
l=list(int(i) for i in input().strip().split(' '))
pairSum0(l)
