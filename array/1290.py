# Problem ID 1290 Pair Sum
def pairSum(arr, x):
    size=len(arr)
    for i in range(0, size):
        candidate = arr[i]
        pair = x - candidate
        for j in range(i+1, size):
            if(pair == arr[j]):
                if(candidate < pair):
                    print(candidate, pair, sep=' ')
                else:
                    print(pair, candidate, sep=' ')

n=int(input())
arr=list(int(i) for i in input().strip().split(' '))
x=int(input())
pairSum(arr, x)
