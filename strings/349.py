# Problem ID: 349 Check Permutation
def permutation(s1, s2):
    freqCount = {}
    for char in s1:
        if char in freqCount:
            freqCount[char] += 1
        else:
            freqCount[char] = 1
    for char in s2:
        if char in freqCount:
            if freqCount[char]==1:
                del freqCount[char]
            else:
                freqCount[char] -= 1
        else:
            return False
    if freqCount:
        return False
    return True

# Main
s1=input()
s2=input()
if permutation(s1, s2):
    print('true')
else:
    print('false')
