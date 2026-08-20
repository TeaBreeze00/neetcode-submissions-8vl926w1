class Solution:
    def canJump(self, nums: List[int]) -> bool:
    # Okay, so from each of the position, I can either jump upto the number in that index. So, the recurrence relation is: dp[i] = Means I can reach the last index starting from index i, we want to figure out dp[0]. So dp[0] in this example: [3,2,0,1,0] would mean I can jump to either dp[1] or dp[2] or dp[3]. dp[Last index] would be true as I can jump to the last index from the last index.

    # We will follow a bottom-up dynamic programming approach. We'll start from the last index, then we move on one-by-one to the left after which dp[0] will give us a solution. We'll also cache this. Standard dp recurrence problem so far

     dp = [False] * len(nums)
     dp[len(nums) - 1] = True
     n = len(nums)

     for i in range(len(nums) - 2, -1, -1):
         temp = False

         for j in range(i + 1, min(n, i + nums[i] + 1)):
             temp = temp or dp[j]
        
         dp[i] = temp
    
     return dp[0]


