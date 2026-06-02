class TrieNode:
    def __init__(self):
        self.children = {}
        self.eow = False

class Solution:
    def __init__(self):
        self.trie = TrieNode()
    
    def create_trie(self, words: List[str]):
        def add_word(word):
            curr = self.trie

            for char in word:
                if char not in curr.children:
                    curr.children[char] = TrieNode()

                curr = curr.children[char] 

            curr.eow = True

        for word in words:
            add_word(word)

    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        self.create_trie(words)
        found = set()
        rows, cols = len(board), len(board[0])

        def dfs(i, j, curr_word, curr):
            outOfBounds = (i < 0 or j < 0 or i >= len(board) or j >= len(board[0]) or 
            board[i][j] not in curr.children)
            
            if outOfBounds:
                return

            if curr.children[board[i][j]].eow:
                found.add(curr_word+board[i][j])

            char = board[i][j]
            board[i][j] = '#'

            dfs(i-1, j, curr_word+char, curr.children[char])
            dfs(i+1, j, curr_word+char, curr.children[char])
            dfs(i, j+1, curr_word+char, curr.children[char])
            dfs(i, j-1, curr_word+char, curr.children[char])
               
            board[i][j] = char


        for row in range(rows):
            for col in range(cols):
                dfs(row, col, '', self.trie)

        return list(found)        