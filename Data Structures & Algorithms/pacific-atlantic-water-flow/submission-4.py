class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        ROWS, COLS = len(heights), len(heights[0])
        directions = ((0, -1), (0, 1), (1, 0), (-1, 0))


        def dfs(i, j, preVal):
            nonlocal pacific, atlantic
            
            if i < 0 or j < 0:
                pacific = True
                return
            
            if i >= ROWS or j >= COLS:
                atlantic = True
                return

            if heights[i][j] > preVal:
                return
            
            currHeight = heights[i][j]
            heights[i][j] = float('inf')

            for dx, dy in directions:
                dfs(i+dx, j+dy, currHeight)
                if pacific and atlantic:
                    break
            
            heights[i][j] = currHeight

        res = []
        for row in range(ROWS):
            for col in range(COLS):
                pacific = atlantic = False
                dfs(row, col, float('inf'))
                if pacific and atlantic:
                    res.append([row, col])
        
        return res
