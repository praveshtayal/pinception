# Problem ID 1679, longestIncreasingSubsequence
def longestIncreasingSubsequence(l, output):
    n = len(l)
    if n==0:
        return 0
    if n==1:
        output.append
        return 0
    include = values[0] + knapsackBF(weights[1:], values[1:],
            maxWeight-weights[0]) if weights[0]<=maxWeight else smallNumber
    exclude = longestIncreasingSubsequence(l[1:], output)
    ans = max(include, exclude)
    return ans;
    if l[0]<l[1]:
        return longestIncreasingSubsequence(l[1:])

    value = [0] * (n+1)
    value[1] = l[n-1]
    for i in range(2,n+1):
        value[i] = max(l[n-i]+value[i-2], value[i-1])

    return value[n]

# Main
n=int(input())
l=list(int(i) for i in input().strip().split(' '))
output = []
longestIncreasingSubsequence(l, output)
print(len(output))
