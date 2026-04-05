class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        if not grid:
            return 0   

        rows = len(grid)
        cols = len(grid[0])
        numofislands = 0
        directions = [[-1, 0],[1, 0],[0, -1],[0, 1]]

        def bfs(i, j):
            q = deque()
            q.append((i, j))
            grid[i][j] = "0"

            while q:
                row, col = q.popleft()
                for a, b in directions:
                    ra, rb = row + a, col + b
                    if(ra < 0 or rb < 0 or ra >= rows or rb >= cols or grid[ra][rb] == "0"):
                        continue
                    q.append((ra, rb))
                    grid[ra][rb] = "0"    




        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == "1":
                    bfs(i, j)
                    numofislands+=1

        return numofislands            