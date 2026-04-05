class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = nums
        heapq.heapify(heap) # O(n)

        while len(heap) > k:
            heapq.heappop(heap) 

        return heapq.heappop(heap)    