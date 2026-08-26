class Solution:
    def numDecodings(self, s: str) -> int:
        # The initial intuition is to use something like substring dp like palindromes. We have i and j indexes in the string that we can use. for each of the substring we construct, we can check it with a hashset to look up quickly if it is indeed a valid substring. So let's run over it with an example, let's say we are given 101, we can break it down to 1, 10, 01, 1. We record only the valid ones. But it has a potential problem where if we are given 01, and if we try to break it down to 0 and 1, and 01 it is not a potential solution right?
        # Let's see another approach, digits can either be 1 digit or two digits, so how we break down the problem is either we choose 1 digit, check if it's valid, if it's valid we break down the problem further. We also can choose 2 digits and if it's valid, we break down the problem further and ask similar question to a smaller problem. This seems promising. So in a sense, for 1 input, the number of ways we can break down 1 string is either choosing 1 digit and break down + choosing 2 digit + break down.
        # so for 1012, num of decoding ways ("1012") = numofdecodingways("012") {if first digit is valid} + numofdecodingways("12") {if choosing 2 digit is valid in this case}
        # so if dp[i] = number of ways to decode, dp[i] = dp[i+1] if s[i] is valid encoding + dp[i+2] if s[i..1] is a valid encoding.
        # For bottom up-dp, i stop when I reach the last char, so I need to iterate from the end of the string to first character of the string
        n = len(s)
        dp = [0] * (n + 2) # 2 char cushioing for the bottom up base case

        dp[n] = 1 # Base case, when we traversed through the whole string we should get 1       
        for i in range(n-1, -1, -1):
            single_valid = s[i] != '0'
            two_digit_valid = i + 1 < n and 10 <= int(s[i:i+2]) <= 26 # double digit cannot have leading 0's

            if single_valid:
                dp[i] += dp[i+1]
            if two_digit_valid:
                dp[i] += dp[i+2] 

        return dp[0]            


