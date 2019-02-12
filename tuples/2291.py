def duplicateCount(arr):
    count = 0
    map = {}
    for number in arr:
        if number in map:
            count += 1
        else:
            map[number] = 1
    return count

# Main
n=int(input())
arr=list(int(i) for i in input().strip().split(' '))
print(duplicateCount(arr))
