class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        # One optimization is to immediately convert the word dict to hashset to have fast lookup times
        # A brute force approach that is coming to mind right now is: Go through the word dictionary, if you find the word that matches, then make the string smaller, then try to find another word in the reduced string, and keep on doing that, if the reduced string is empty, then it means that we have found all of the match and return true. But, the problem is let's say in example 3, if we have a situation where we have both cats and cat, which one do we match to? Same question with "sin" and "in", seems like we have multiple ways of reducing our search space.
        # So there is a recurrence relationship possible in this case, base case is empty string in which case we return True. Let's think about the recursive case, in each level, we have upto the word of the dictionary choices to make to find the first match. Let's say for the 3rd example, we find matches of the first portion of the string with both "cats" and "cat", we will try out both of the possibilities and if either one of them returns a true, we return true, in case we don't find a match and can't break down the word further, we return false. So, if wordbreak(str) = wordbreak(str - matches) for all matches in the word dict with OR in between them.
        # Let's run this with this example: "catsincar", cats and cat is both in the dict, so we search over both the possibilities, sincar and incar, both of these will return truw and so the example will return true, for catsincars, same thing we have sincars and incars, both of them will return false and so we will return false as expected. 
        # Good, but this is sadly exponential: wordBreak("aaaaaab", ["a","aa","aaa","aaaa"]). So wordBreak(7) = wordBreak(6) or wordBreak(5) or wordBreak(4) or wordBreak(3), where wordBreak(6) would have identical subproblems as the other problems, lots of overlap, that calls for good old dp
        # For a dp solution, the base case is the smallest string possible to the right, so we can build up our dp solution bottom up by traversing the string from right to left and build up, dp[i] denotes the state if a word starting from this index is possible to break. If dp[0] = true it means the whole string starting from 0 is possible to break and hence the solution.
        # So, when iterating, for each i, we see if there's a match between the substring starting from i to the end between any word in the dict, if there's a match, we return the OR of each of the smaller cases. So, we loop through again from i and check all possible cases.

        dp = [False] * (len(s) + 1)
        dp[len(s)] = True
        dictionary = set() # building the dictionary set for fast lookups

        for word in wordDict:
            dictionary.add(word)

        for i in range(len(s), -1, -1):
            for j in range(i, len(s)):
                if s[i:j + 1] in dictionary:
                    dp[i] = dp[i] or dp[j+1]

        return dp[0]               
