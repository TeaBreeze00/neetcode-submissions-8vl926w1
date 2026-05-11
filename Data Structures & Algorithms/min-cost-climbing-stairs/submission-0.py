class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        # so here is the dealio, I can either start from 0 or 1 index, then I can
        # make two choices, either take 1 step or take 2 steps from 0 or 1 indexes.
        # so there are 4 decisions that I can take from one step. I can either take the index
        # and then take 1 or 2 step (whatever gives me the minimum) or I can skip this index, take the 
        # next step pay the cost and then I do I step or 2 step depending on the cost. 
        # cost = [1, 2, 3]
        # dp =   [0, 0, ..]
        # dp[i] signifies the cheapest cost to reach at ith level of the staircase, cost[i] signifies the cost to be paid to 
        # leave the staircase. so dp[i] + cost[i] would signify the cost paid to get to i-th stair and also the cost paid to leave
        # it.
        n = len(cost)
        dp = [0] * (n+1)
        
        for i in range(2, n+1):
            dp[i] = min((dp[i-1]+cost[i-1]),(dp[i-2]+cost[i-2]))

        return dp[n]