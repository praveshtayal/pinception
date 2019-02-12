# Problem ID 1137, replaceCharacter
def replaceCharacter(string, c1, c2):
    if len(string)==0:
        return string
    string2 = replaceCharacter(string[1:],c1,c2)
    if string[0]==c1:
        return c2 + string2
    else:
        return string[0] + string2

# Main
from sys import setrecursionlimit
setrecursionlimit(11000)
string = input().strip()
c1, c2 = (i for i in input().strip().split(' '))
print(replaceCharacter(string, c1, c2))
