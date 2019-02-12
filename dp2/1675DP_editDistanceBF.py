# Problem ID: , editDistance
def editDistanceBF(s1, s2):
    ''' Return editDistance using Brute Force'''
    m = len(s1)
    n = len(s2)
    if m==0:
        return n
    if n==0:
        return m
    if s1[0] == s2[0]:
        return editDistanceBF(s1[1:], s2[1:])
    op1 = editDistanceBF(s1[1:], s2)
    op2 = editDistanceBF(s1, s2[1:])
    op3 = editDistanceBF(s1[1:], s2[1:])
    ans = 1+min(op1, op2, op3)
    return ans;

# Main
from sys import setrecursionlimit
setrecursionlimit(11000)
s1 =input().strip()
s2 =input().strip()
print(editDistanceBF(s1, s2))
