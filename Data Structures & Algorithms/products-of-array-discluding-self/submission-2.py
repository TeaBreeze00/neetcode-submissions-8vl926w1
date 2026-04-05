class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        # This is classic prefix and postfix sum, we can declare 2 separate prefix and 
        # postfix array to find prefix multiplication and postfix multiplication and then a result
        # array to figure out, but we'll go and make prefix and postfix multiplication on the spot and 
        # calculate everything in the result array itself

        res = []
        res.append(1)

        for i in range(1, len(nums)):
            res.append(res[i-1] * nums[i-1])

        postfix = 1

        for i in range(len(nums)-1, -1, -1):
            res[i] = postfix * res[i]
            postfix *= nums[i]

        return res        



        
               





            
