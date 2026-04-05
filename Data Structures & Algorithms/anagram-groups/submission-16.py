class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        res = defaultdict(list)
        for s in strs:
            char = [0] * 26 # For each string I have a 26 length word structure

            for c in s:       # For each character in the string
               char[ord(c) - ord('a')] += 1

            res[tuple(char)].append(s)       
        
        return list(res.values())
