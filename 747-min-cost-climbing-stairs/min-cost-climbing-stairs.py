class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = 2
        last, curr = cost[0], cost[1]

        while n < len(cost):
            last, curr = curr, cost[n] + min(last, curr)
            n+=1
        return min(last, curr)  