class Solution:
    def longestPalindrome(self, s: str) -> str:
        # For the brute force approach, what we can do is iterate over the whole string and find all of the subloops, then we use two pointers to see if the substring is indeed a palindrome. If the substring is indeed a palindrome, we can keep track of it if it is the longest substring yet discovered. For this approach, the time complexity is O(n^3) as we need double for loops to get all of the substrings and also 2 pointer approach takes linear time in general.
        # Let's see this being played out in action:
        """
        maxlength = 0
        longestsubstring = ""

        for i in range(len(s)):
            for j in range(i, len(s)):
                left_ptr = i
                right_ptr = j
                is_palindrome = True
                while left_ptr <= right_ptr:
                    if s[left_ptr] == s[right_ptr]:
                        left_ptr += 1
                        right_ptr -= 1
                    else:
                        is_palindrome = False
                        break
                if is_palindrome:
                    length = (j - i) + 1
                if length > maxlength:
                    maxlength = length
                    longestsubstring = s[i:j+1]   
        """
        # We ARE doing a lot of repeated work here. Hmm, if only if there was a way to store results of smaller sections so that we can calculate the result of the bigger section? Bingo, let's do a dynamic programming approach here to store info about substrings so that we can expand our search. The key idea is dp[i][j] denotes if s[i:j+1] is palindrome or not. So, in order of expansion, if s[i] == s[j] and dp[i+1, j-1] = True, then we can put dp[i][j] = True as it will be a palindrome. For base cases, we can have 1 or 2 characters (j-i+1) and we'll set dp to true if the characters match only as there is no middle character., capiche?
        m = n = len(s)
        dp = [[False]* (n) for _ in range(m)] # m*n matrix is formed
        maxlength = 0
        longeststring = ""
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
        
                if dp[i][j] and (j - i + 1) > maxlength: # just track the longest substring till now and return it!
                    maxlength = j - i + 1
                    longeststring = s[i:j+1]

        return longeststring   





