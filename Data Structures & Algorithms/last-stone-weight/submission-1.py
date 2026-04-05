class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        # Heapify the list first
        maxheap = [-stone for stone in stones]
        heapq.heapify(maxheap) # O(n)
        
        one, two = 0, 0

        while maxheap:

            if len(maxheap) < 2:
                break
                
            one = -heapq.heappop(maxheap)
            two = -heapq.heappop(maxheap)
            if one != two:
                heapq.heappush(maxheap, -(one - two))    

        if maxheap:
            return -maxheap[0]

        return 0         