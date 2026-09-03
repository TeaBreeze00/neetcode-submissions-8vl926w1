class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        # LIS is the max length of the longest increasing sequence. How will we generate subsequence that is also increasing with recursion? Let's say that I have the full list starting from index 0. Can I not chain like, I ask the element next to me what length of an increasing subsequence can you make (if it's greater than me) if it's not greater than me I can ask the next one, I can ask all the way to the end and take max of longest increasing subsequence. 
        # Okay, seems straightforward, we'll start by defining the dp state. dp[i] denotes the longest increasing subsequence we can form starting at index i. The base case is from right most element so for bottom up dp, we start from right to left.
        # We can give the last element base case of 1 and start from there as the last element will be able to form a subsequence of length 1. 
        
        n = len(nums)
        dp = [1] * n
        dp[n-1] = 1 # Set the base case to 1

        for i in range(n-1, -1, -1):
            for j in range(i, n):
                if nums[j] > nums[i]:
                    dp[i] = max(dp[i], 1 + dp[j])

        return max(dp)            