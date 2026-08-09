class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        res  = []
        curr = [] # The result that needs to be returned and also
                       # the current stack that tracks the current state
        
        def backtrack(i):
            # base case
            if i == n:
                res.append(curr[:])
                return

            # don't pick it
            backtrack(i+1)

            # pick it
            curr.append(nums[i])
            backtrack(i+1)
            curr.pop()

        backtrack(0)
        return res    
