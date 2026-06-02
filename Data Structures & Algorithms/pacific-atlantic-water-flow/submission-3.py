class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        rows, cols = len(heights), len(heights[0])

        def dfs(i, j):
            if i == 0 or j == 0:
                v[0] = 1
            
            if i == rows-1 or j == cols-1:
                v[1] = 1

            if sum(v) == 2 or (i, j) in dont_check:
                return 
        
            curr_height = heights[i][j]
            
            # Conditions for all the four directions.
            cond1 = (i+1) < rows and heights[i+1][j] <= curr_height
            cond2 = (i-1) >= 0 and heights[i-1][j] <= curr_height
            cond3 = (j+1) < cols and heights[i][j+1] <= curr_height
            cond4 = (j-1) >= 0 and heights[i][j-1] <= curr_height
            
            heights[i][j] = 1001
            f = 0
            if cond1:
                f = 1
                dfs(i+1, j)
            if cond2:
                f = 1
                dfs(i-1, j)
            if cond3:
                f = 1
                dfs(i, j+1)
            if cond4:
                f = 1
                dfs(i, j-1)

            if f == 0:
                dont_check.add((i, j))

            heights[i][j] = curr_height

        dont_check = {(0, cols-1), (rows-1, 0)}
        res = {(0, cols-1), (rows-1, 0)}

        for row in range(rows):
            for col in range(cols):
                v = [0, 0]
                dfs(row, col)
                print(heights[row][col])
                if sum(v) == 2:
                    res.add((row, col))

        return list(res)