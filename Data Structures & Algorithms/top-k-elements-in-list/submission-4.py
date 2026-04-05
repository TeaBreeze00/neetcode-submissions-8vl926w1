from collections import defaultdict, Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        # This is the brute force plan, I'll build out a hashmap that contains all the possible 
        # numbers and their frequencies. Then I'll have a heap and if the heap ever goes out of 
        # k, then we pop one element, we build a min heap so that only the top ones remain

        mymap = defaultdict(int)

        for num in nums:
            if mymap[num]:
                mymap[num] += 1
            else:
                mymap[num] = 1    


        heap = []

        for num in mymap:
            heapq.heappush(heap, (mymap[num], num))
            if len(heap) > k:
                heapq.heappop(heap)
        
        res = []

        for i in range(k):
            res.append(heapq.heappop(heap)[1])

        return res    
        
            



       
