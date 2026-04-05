class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # initializing 2 pointers one at the front another one at the end
        i = 0
        j = len(heights) - 1

        max = 0
        #The formula for checking the height is (j-i)*min[heights[i],heights[j]]
        while i < j:
            left = heights[i]
            right = heights[j]

            area = (j - i) * min(left, right)

            if(area > max):
                max = area

            if (heights[i] > heights[j]):
                j -= 1
                continue

            elif (heights[i] < heights[j]):
                i += 1
                continue

            #what happens if they're equal? Do a random move, left or right doesn't matter
            j -= 1

        return max