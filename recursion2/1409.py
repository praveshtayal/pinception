# Problem ID 1409: print Permutation
def printPermutationsHelper(s, output):
    length = len(s)
    if length==0:
        print(output)
        return
    for i in range(0, length):
        printPermutationsHelper(s[0:i] + s[i+1:], output + s[i])

def printPermutations(s):
    printPermutationsHelper(s,"")

# Main
s = input()
printPermutations(s)
