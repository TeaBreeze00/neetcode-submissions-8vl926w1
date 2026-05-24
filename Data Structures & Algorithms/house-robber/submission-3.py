class Solution:
    def rob(self, nums: List[int]) -> int:
     # Let's do a bottom up dynamic programming approach to this problem
     # We'll use the same idea from the recursion, dp[i] denotes the max amount of money you can rob
     # from houses 0...i
     if len(nums) == 1:
        return nums[0]

     dp = [0] * len(nums)
     dp[0] = nums[0]
     dp[1] = max(nums[1], nums[0])

     for i in range(2, len(nums)):
        dp[i] = max(nums[i]+dp[i-2], dp[i-1])

     return dp[-1]   