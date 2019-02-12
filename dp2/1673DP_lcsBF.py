# Problem ID: 1673, lcs
def lcsBF(s1, s2):
    ''' Return lcs using Brute Force'''
    m = len(s1)
    n = len(s2)
    if m==0 or n==0:
        return 0
    if s1[0] == s2[0]:
        return 1+lcsBF(s1[1:], s2[1:])
    op1 = lcsBF(s1[1:], s2)
    op2 = lcsBF(s1, s2[1:])
    ans = max(op1, op2)
    return ans;

# Main
from sys import setrecursionlimit
setrecursionlimit(11000)
s1 =input().strip()
s2 =input().strip()
print(lcsBF(s1, s2))
