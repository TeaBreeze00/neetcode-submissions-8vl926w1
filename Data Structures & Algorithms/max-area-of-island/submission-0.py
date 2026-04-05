class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        
        if not grid:
            return 0
        
        # get the rows and columns
        rows = len(grid)
        cols = len(grid[0])

        # 4 directions left, right, up and down
        direction = [[-1,0], [1, 0], [0, -1], [0, 1]]
        maxarea = 0

        def dfs(i, j):
            stack = []
            stack.append((i, j))
            grid[i][j] = 0
            area = 1

            while stack:
                row, col = stack.pop()
                for dr, dc in direction:
                    r, c = row + dr, col + dc
                    if 0 <= r < rows and 0 <= c < cols and grid[r][c] == 1:
                        stack.append((r, c))
                        grid[r][c] = 0
                        area += 1   

            return area

        for i in range(rows):
            for j in range(cols):
                if(grid[i][j] == 1):
                    maxarea = max(maxarea, dfs(i, j))  

        return maxarea             

         


