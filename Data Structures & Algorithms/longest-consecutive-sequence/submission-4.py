from typing import List
from collections import defaultdict

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numsnew = sorted(set(nums))  # sort and remove duplicates

        if len(numsnew) == 0:
            return 0

        mymap = {}
        seq = set()
        prev = numsnew[0]
        seq.add(prev)

        for i in range(1, len(numsnew)): # I start from 1 to len(numsnew)
            if numsnew[i] - prev == 1:
                seq.add(numsnew[i])
                prev = numsnew[i]
            else:
                mymap[len(seq)] = seq
                seq = set()
                seq.add(numsnew[i])
                prev = numsnew[i]

        # Add the last sequence
        mymap[len(seq)] = seq

        return max(mymap.keys())
