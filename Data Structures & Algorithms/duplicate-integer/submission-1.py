class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seen = set()

        for num in nums:
            if num in seen:
                return True  # Corrected boolean
            seen.add(num)
        
        return False  # Corrected boolean