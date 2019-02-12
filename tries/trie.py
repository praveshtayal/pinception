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
        return curr.terminal

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
trie.insert('and')
trie.insert('bat')
trie.insert('ball')
trie.printTrie()
#print(trie.search('and'))
#print(trie.search('android'))
#trie.deleteRecursive('bat')
trie.deleteRecursive('ball')
trie.printTrie()
