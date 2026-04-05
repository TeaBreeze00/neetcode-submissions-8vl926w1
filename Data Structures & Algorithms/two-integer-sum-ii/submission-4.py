class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:

        l, r = 0, len(numbers) - 1

        while (l < r):

            tgt = numbers[l] + numbers[r]

            if(tgt > target):
                r -= 1
                continue

            if(tgt < target):
                l += 1
                continue

            break    

        return [l+1, r+1]


        