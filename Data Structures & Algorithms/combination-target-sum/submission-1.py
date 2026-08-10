class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:

        # This is definitely a backtracking solution. I can maintain 2 arrays as usual. Then once in base case, I can return if the subset satisfies the condition. Else, I can keep on exploring the other options as usual
        res, curr = [], []
        n = len(nums)

        def backtrack(i, curr_sum):

            if curr_sum == target:
                res.append(curr[:])
                return
            
            if curr_sum > target or i == n:
                return 

            backtrack(i+1, curr_sum)

            curr.append(nums[i])
            backtrack(i, curr_sum + nums[i])
            curr.pop()

        backtrack(0, 0)
        return res    



        