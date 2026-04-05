from typing import List
from collections import defaultdict

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        # So this is the game plan: I have a list. I will everything that I have in the list in a hashset
        # Then I will iterate over the set. If I can make a consecutive sequence, then I will keep going on to 
        # make the consecutive sequence. I will also keep removing the digits that I find in the hashmap
        # Then I will guarantee that the only thing that I will keep finding in the hashset is unique sequences
        
        num = set(nums)
        longest = -math.inf
        
        if not nums:
            return 0
        
            
        for n in num:
            numtofind = n
            
            count = 0
            
            # Only start the iteration if the previous thing is not present in the hashset, i.e. it is the begining of a sequence
            if n-1 not in num:

                while numtofind in num:
                    k = numtofind
                    numtofind += 1
                    count += 1

            longest = max(longest, count)

        return longest      
