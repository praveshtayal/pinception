# Problem ID: 60 highest frequency character
def maxChar(s):
    freqCount = {}
    ans = s[0]
    for char in s:
        if char in freqCount:
            freqCount[char] += 1
            if freqCount[char] > freqCount[ans]:
                ans = char
        else:
            freqCount[char] = 1
    for char in s:
        if char==ans:
            return ans
        if freqCount[char]==freqCount[ans]:
            return char
    return ans

# Main
s=input()
print(maxChar(s))
