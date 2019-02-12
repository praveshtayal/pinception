# Problem ID 36 Check Palindrome using recursion 
def RcheckPalindrome(str):
    size=len(str)
    if size <= 1:
        return True
    if str[0]!=str[size-1]:
        return False
    return RcheckPalindrome(str[1:-1])

# Main
from sys import setrecursionlimit
setrecursionlimit(11000)
str=input()
if RcheckPalindrome(str):
    print('true')
else:
    print('false')
