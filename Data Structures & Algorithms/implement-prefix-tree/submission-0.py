class PrefixTree:
    class TrieNode:
        def __init__(self, letter=None, eow=None):
            self.letter = letter
            self.child = [None]*26
            self.eow = eow

    def __init__(self):
       self.root = self.TrieNode(eow=0) 


    def insert(self, word: str) -> None:
        curr = self.root
        i = 0

        while i < len(word) and curr.child[ord(word[i])-ord('a')]:
            curr = curr.child[ord(word[i])-ord('a')]
            i+=1

        if i != len(word):
            while i < len(word) :
                curr.child[ord(word[i])-ord('a')] = self.TrieNode(letter=word[i], eow=0)
                curr = curr.child[ord(word[i])-ord('a')]
                i+=1

        curr.eow = 1

                
    def search(self, word: str) -> bool:
        i =0
        curr = self.root

        while i < len(word) and curr.child[ord(word[i])-ord('a')]:
            curr = curr.child[ord(word[i])-ord('a')]
            i+=1

        if i != len(word) :
            return  False

        else :
            return curr.eow == 1     

    def startsWith(self, prefix: str) -> bool:
        i =0
        curr = self.root

        while i < len(prefix) and curr.child[ord(prefix[i])-ord('a')]:
            curr = curr.child[ord(prefix[i])-ord('a')]
            i+=1

        if i != len(prefix) :
            return False

        else :
            return True 
        