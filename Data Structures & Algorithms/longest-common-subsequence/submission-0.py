class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:

# This is a classic 2D dp problem. Let's go over some examples, we have "cat" and "crabt", one thing that is coming off the top of my head is if I have a case where the letters match (c's match in this case) length of common subsequence grows by one and we can safely ignore them and continue our search in the rest of the substring to find more matches. But what if they don't match? Let's say I have "cat" and "rabt", c and r don't match in this case. But I need to narrow down my search anyways to make progress. In that case, I can ignore the char of the first word, and search compare with the other word OR it might be that I can ignore the second word's first character and take all of the first word? That should give us all search scenarios. For dp, dp[i][j] denotes the length of the longest common subsequence taking the first word upto i-index and second word's j index. So the recurrence relationship is dp[i][j] = 1 + dp[i+1][j+1] if text1[i] == text2[j], otherwise dp[i][j] = max(dp[i+1][j], dp[i][j+1]). The base case is reached when we reach the end of both words. For bottom up, we start from our base case and expand the problem. So we need to start our search from the end of both words and work our way backwards. Cool?

        m = len(text1)
        n = len(text2)

        dp = [[0] * (n+1) for _ in range(m+1)]

        for i in range(m-1, -1, -1):
            for j in range(n-1, -1, -1):
                if text1[i] == text2[j]:
                    dp[i][j] = 1 + dp[i+1][j+1]
                else:       
                    dp[i][j] = max(dp[i+1][j], dp[i][j+1])

        return dp[0][0]

        


        