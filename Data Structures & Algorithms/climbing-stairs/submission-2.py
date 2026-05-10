class Solution:
    def climbStairs(self, n: int) -> int:
        # the brute force approach climbstairs(n-1) + climbstairs(n-2) takes 2^n time complexity. Let's do a memoized approach that takes 
        # O(n) time complexity
        # 1.
        dp = [0] * (n + 1)
        dp[0] = 1
        dp[1] = 1

        for i in range(2, n + 1):
            dp[i] = dp[i-1] + dp[i-2]

        return dp[n]    