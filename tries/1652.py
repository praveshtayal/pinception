# Problem ID 1652 Tries search
class TrieNode():
    def __init__(self, char='\0'):
        self.char = char
        self.terminal = False
        self.children = {}

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


choice=int(input())
t=Trie()
while choice != -1:
    if choice==1:
        # insert
        word=input()
        t.insert(word)
    elif choice==2:
        word=input()
        ans=t.search(word)
        if ans:
            print("true")
        else:
            print("false")
    else:
        quit()
    choice=int(input())
