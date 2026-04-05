class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        myset = defaultdict()

        for i in range(len(nums)):            # Need to iterate through the array
            remainder = target - nums[i]

            if remainder in myset:            # Proper indentation for this line
                return [myset[remainder], i]  # If I find the remainder in the hashmap, I return the indices

            myset[nums[i]] = i                # If I don't find the remainder, I continue with the iteration

        return []
