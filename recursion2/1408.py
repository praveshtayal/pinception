# Problem ID 1408: return Permutation  
def returnPermutations(s):
    l = []
    length = len(s)
    if length==1:
        return [s]
    for i in range(0, length):
        permutations = returnPermutations(s[0:i]+s[i+1:])
        for perm in permutations:
            l.append(s[i] + perm)
    return l

# Main
s = input()
permutations = returnPermutations(s)
print(*permutations, sep='\n')
