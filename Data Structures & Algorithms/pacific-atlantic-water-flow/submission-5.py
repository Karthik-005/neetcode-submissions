class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        ROWS, COLS = len(heights), len(heights[0])
        directions = ((0, -1), (0, 1), (1, 0), (-1, 0))

        def dfs(i, j, preVal, ocean):
            if i >= ROWS or j >= COLS or i < 0 or j < 0 or (i, j) in ocean or heights[i][j] < preVal:
                return
        
            
            ocean.add((i, j))

            for dx, dy in directions:
                dfs(i + dx, j + dy, heights[i][j], ocean)
        

        pacific = set()
        atlantic = set()

        for col in range(COLS):
            dfs(0, col, -1, pacific)
            dfs(ROWS-1, col, -1, atlantic)
        
        for row in range(ROWS):
            dfs(row, 0, -1, pacific)
            dfs(row, COLS-1, -1, atlantic)


        return list(pacific & atlantic)


            

                
            
            
