class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        #This is the plan, I have a hashmap.  I store the values of the array as key and frequency as the value,
        #Then I return the top k values of the hashmap

        mymap = defaultdict(int)
        
        for n in nums:
            mymap[n] += 1

        sorted_items = sorted(mymap.items(), key=lambda item: item[1], reverse=True)
        top_k = [key for key, value in sorted_items[:k]] 

        return top_k 
       
