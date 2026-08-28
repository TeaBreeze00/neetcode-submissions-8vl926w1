class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # In each of the stage, we have 3 choices, I can choose the first coin or the second coin, or the third coin. For each of the choice that I make, I'll have to subtract that amount in the later stage. Let's define a dp state as dp[i] = minimum number of coins needed to make amount i. At each of the stage, what I am doing basically is, dp[12] = 1 + dp[11], because this says to find the minimum number of coins needed to make 12, I choose 1 coin and then take the minimum of the rest, and do this for all of my choices. Let's think about the base cases in this recurrence. We need to think about impossible amount and also the smallest coin amount we are given will also be a base case imo. dp[0], dp[1] and also dp[-amount]?
        """
        Defining the recurrence relationship, we have dp[i] = min(1+dp[i-coins[j]]) for j = 0 to length of coins array, in other words, take the minimum of all of the choices that you can make with the coins! 
        """
        n = len(coins)
        dp = [float('inf')] * (amount + 1)
        dp[0] = 0

        for i in range(1, amount+1):
            for coin in coins:
                if i - coin >= 0: # If i - coin < 0, that path is set to inf, so naturally avoided
                    dp[i] = min(dp[i], 1 + dp[i - coin])

        if dp[amount] == float('inf'):
            return -1

        return dp[amount]


