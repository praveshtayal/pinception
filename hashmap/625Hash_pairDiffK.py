# Problem ID 625: Pairs with difference K
def printPairDiffK(l, k):
    if k<0: # k is now non negative
        k *= -1
    #m = {num:True for num in l}
    m = {}
    for num in l:
        if num+k in m:
            for i in range(0,m[num+k]):
                print(num, num+k)
        if k!=0 and num-k in m:
            for i in range(0,m[num-k]):
                print(num-k, num)

        # Update map        
        if num in m:
            m[num] += 1
        else:
            m[num] = 1

# Main
n=int(input())
l=list(int(i) for i in input().strip().split(' '))
k=int(input())
printPairDiffK(l, k)
