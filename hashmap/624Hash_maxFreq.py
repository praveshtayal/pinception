# Problem ID 624: Highest Frequency Number in a list 
def maxFreq(l):
    ans = l[0]
    map = {}
    for num in l:
        if num in map:
            map[num] += 1
        else:
            map[num] = 1
        if map[num] > map[ans]:
            ans = num
    return ans

# Main
n=int(input())
l=list(int(i) for i in input().strip().split(' '))
print(maxFreq(l))
