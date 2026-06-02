class TrieNode:
    def __init__(self):
        self.children = {}
        self.eof = False

class WordDictionary:

    def __init__(self):
        self.trie = TrieNode()

    def addWord(self, word: str) -> None:
        curr = self.trie

        for char in word:
            if char not in curr.children:
                curr.children[char] = TrieNode()
            curr = curr.children[char]
        
        curr.eof = True

    def search(self, word: str) -> bool:
        def dfs(j, root):
            curr = root

            for i in range(j, len(word)):
                if word[i] == '.':
                    if not curr.children:
                        return False

                    else:
                        for char in curr.children:
                            if dfs(i+1, curr.children[char]):
                                return True
                            
                        return False

                else:
                    if word[i] not in curr.children:
                        return False
                    curr = curr.children[word[i]]                

            return curr.eof

        return dfs(0, self.trie)                

    