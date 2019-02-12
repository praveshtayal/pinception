def freqMap(l):
    map = {}
    for num in l:
        if num in map:
            map[num] += 1
        else:
            map[num] = 1
    return map

def evenCount(arr):
    map = freqMap(arr)
    for number in arr:
        if map[number]%2==0:
            return number
    return -1

# Main
n=int(input())
arr=list(int(i) for i in input().strip().split(' '))
print(evenCount(arr))
