# Problem ID: 62 reverse each word
def reverse(s):
    ans = ''
    for char in s:
        ans = char + ans
    return ans

def reverseEachWord(s):
    length = len(s)
    index=0
    while index<length:
        if s[index] in ' \t\n':
            index += 1 # Ignore white spaces
        else:
            start = index # Start of word found
            index += 1
            while index<length and s[index] not in ' \t\n':
                index += 1
            s = s[:start] + reverse(s[start:index]) + s[index:]
    return s

# Main
s=input()
print(reverseEachWord(s))
