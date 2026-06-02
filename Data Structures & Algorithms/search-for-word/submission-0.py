class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows, cols = len(board), len(board[0])
        visited = [[False for _ in range(cols)] for _ in range(rows)]

        def search(i, j, k) :
            if k == len(word) :
                return True

            if  (i < 0 or j < 0 or i >= rows or j >= cols or 
                board[i][j] != word[k] or visited[i][j]) :
                return False

            visited[i][j] = True

            res = (
                search(i-1, j, k+1) or 
                search(i+1, j, k+1) or
                search(i, j-1, k+1) or
                search(i, j+1, k+1)
            )    
            visited[i][j] = False

            return res

        for i in range(rows) :
            for j in range(cols) :
                if search(i, j, 0) :
                    return True

        return False                