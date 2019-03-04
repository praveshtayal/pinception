# Probelm ID 532, shortestSubsequence

# s is a string for which subsequences are to be generated
# m is the map storing string:subsequence mapping
# This function generate subsequences using Memoization
def subsequence(s, m):
    if s in m:
        return m[s]
    if len(s)==0:
        m[s] = { '' }
        return m[s]

    s1 = subsequence(s[1:])
    s2 = set()
    for string in s1:
        s2.add(s[0]+string)
    m[s] = s1.union(s2)
    return m[s]

def indexMap(s):
    map = {}
    for index, char in enumerate(s):
        if char in map:
            map[char].append(index)
        else:
            map[char] = [index]
    return map

def isSubsequence(subseq, m):
    index = 0
    for char in subseq:


def shortestSubsequence(s, v):
    subsequences = subsequence(s)
    sortedSubsequences = {i:[] for i in range(len(s)+1)}
    for _ in subsequences:
        sortedSubsequences[len(_)].append(_)
    #print(subsequences)
    print(sortedSubsequences)

    m = indexMap(v)
    lv = len(v)
    print(m)
    return ''

# Main
s=input()
v=input()
ans=shortestSubsequence(s,v)
print(ans)
print(len(ans))
