class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # Here is the dealio, I have a grid where I can only go either down or right. Let's see what to do here. When I am in one grid, I can ask the top position about the number of paths it has, and then if I move down I basically extend that path. So, if I have 2 paths on the top cell, if I go down I'll have 2 paths still. Also I can ask the left cell and apply the same logic. So at the current cell, I can return the sum of paths from top and bottom. For a dp solution, what the implication is that dp[i][j] denotes the total number of paths in cell (i,j). So, grid[m][n] = grid[m][n-1] + grid[m-1][n]. This should give us all possibilities. We can start from base case, top left corner and work our way upto the last cell. Capiche?
        dp = [[0] * (n+1) for _ in range(m+1)]

        # First row
        for j in range(n + 1):
            dp[0][j] = 1

        # First column
        for i in range(m + 1):
            dp[i][0] = 1

        for i in range(1,m):
            for j in range(1,n):
                dp[i][j] = dp[i][j-1] + dp[i-1][j]

        return dp[m-1][n-1]        