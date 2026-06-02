class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        count = 0
        rows, cols = len(grid), len(grid[0])

        def dfs(i, j):
            outOfBounds = (i < 0 or j < 0 or i >= rows or j >= cols or
            grid[i][j] == '0')

            if outOfBounds:
                return

            grid[i][j] = '0'
            dfs(i+1, j)
            dfs(i, j+1)
            dfs(i-1, j)
            dfs(i, j-1)    

        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == '1':
                    count += 1
                    dfs(row, col)

        return count            


        
