class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        # This is the brute force plan, I am going to iterate through the 
        # array and have a pointer. Everytime I have an element, I am going to iterate through
        # the rest of the array and multiply to put it in the list. To do this I am going to 
        # maintain a suffix and prefix. The suffix will iterate through the list and go to the end
        # the prefix will go through the list from previous to the first element

        arrayToReturn = []
        
        #initialize the first pointer to start from the first element of the list
        i = 0

        while i < len(nums):

            numToAdd = 1 #initialize the number to be multiplied
            j = i + 1    # This is the index of the next element
            k = i - 1    # This is the index of the previous element

            while j < len(nums):
                numToAdd *= nums[j]
                j+=1

            while(k >= 0):
                numToAdd *= nums[k]
                k-=1

            arrayToReturn.append(numToAdd)

            i+=1

        return arrayToReturn        





            
