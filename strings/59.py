# Problem ID: 59 Remove duplicate consecutive chars
def removeDuplicates(s):
    index=1
    while index<len(s):
        if s[index] == s[index-1]:
            nextIndex = index+1
            length = len(s)
            while nextIndex<length and s[nextIndex]==s[index]:
                nextIndex += 1
            s = s[:index] + s[nextIndex:]
        else:
            index += 1
    return s

# Main
s1=input()
print(removeDuplicates(s1))
