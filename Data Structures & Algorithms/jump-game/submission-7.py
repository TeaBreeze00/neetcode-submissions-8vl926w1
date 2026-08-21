class Solution:
    def canJump(self, nums: List[int]) -> bool:
        # Let's follow the greedy appraoch now. The idea is that I'll have to constantly move the end post to the begining gradually. So by the time I reach the first index, I already know the closest thing to jump on to reach the end. One analogy to be used here is moving the goalpost. So to move the goalpost, I only want to move it if idx + number at that position == goalpost, only then will we set the element in that array as the new goalpost.
        goalpost = len(nums) - 1 # Set the goalpost as the last element

        for i in range(len(nums) - 1, -1, -1): 
            if i + nums[i] >= goalpost:
                goalpost = i

        return goalpost == 0        




