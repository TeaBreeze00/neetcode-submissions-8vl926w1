class Solution:
    def countSubstrings(self, s: str) -> int:
        # Same as the one we did previously. Previously, we only reported the maximum length of a palindrome. Here, we have to do increase counts whenever we see a palindrome and keep a counter. Same logic used previously applies here.
        m = n = len(s)
        dp = [[False]* (n) for _ in range(m)] # m*n matrix is formed
        count = 0
        """
        dp = [[0, 0, 0]
              [0, 0, 0]
              [0, 0, 0]]
        """
        # Here is the loop structuring, i needs i+1's value and j needs j-1's value first, so we have to iterate i from end to begining and j from small to large for a bottom-up dp approach
        for i in range(m-1, -1, -1):
            for j in range(i, n):
                if (((j - i) + 1) == 1 or ((j - i) + 1) == 2 and s[i]==s[j]): # for 1 or 2 character just matching the extremities is enough
                    dp[i][j] = True
                elif(s[i]==s[j] and dp[i+1][j-1]):
                    dp[i][j] = True
        
                if dp[i][j]: # If this substring is indeed a palindrome, just increment the counter!
                    count += 1 
                    

        return count