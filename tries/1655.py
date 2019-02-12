# Problem ID 1655 Pattern Matching
class TrieNode():
    count = 0
    def __init__(self, char='\0'):
        self.char = char
        self.terminal = False
        self.children = {}
        TrieNode.count += 1

class Trie():
    def __init__(self):
        self.__root = TrieNode()

    def insert(self, word):
        curr = self.__root
        for char in word:
            if char in curr.children:
                curr = curr.children[char]
            else:
                curr.children[char] = TrieNode(char)
                curr = curr.children[char]
        curr.terminal = True

    def search(self, word):
        curr = self.__root
        for char in word:
            if char not in curr.children:
                return False
            else:
                curr = curr.children[char]
        return True # This function does not check if it is terminal

    def patternMatching(self, vect, pattern):
        for word in vect:
            wordLength = len(word)
            for j in range(0, wordLength):
                Trie.insert(self, word[j:])
        #Trie.printTrie(self)
        return Trie.search(self, pattern)

    def delete(self, word):
        curr = self.__root
        for char in word:
            if char not in curr.children:
                return False
            else:
                curr = curr.children[char]
        if curr.terminal:
            curr.terminal = False
            return True
        return False

    def deleteRecursive(self, word):
        Trie.__deleteRecursive(self.__root, word)


    def __deleteRecursive(root, word):
        if len(word)==0:
            root.terminal = False
            return
        if word[0] not in root.children:
            return
        child = root.children[word[0]]
        Trie.__deleteRecursive(child, word[1:])
        if child.terminal==False and len(child.children)==0:
            root.children.pop(word[0])

    def printTrie(self):
        root = self.__root
        for char in root.children:
            Trie.__printRoot(root.children[char], '')

    def __printRoot(root, word):
        newword = word + root.char
        if root.terminal:
            print(newword)
        for char in root.children:
            Trie.__printRoot(root.children[char], newword)

trie = Trie()
n=int(input())
vect=list(input().split(' '))
pattern=input()
found = trie.patternMatching(vect, pattern);
if found:
    print('true')
else:
    print('false')
