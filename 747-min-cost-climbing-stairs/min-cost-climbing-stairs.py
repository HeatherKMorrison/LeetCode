class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = 1
        last, curr = cost[0], cost[1]

        while n+1 < len(cost):
            last, curr = curr, cost[n+1] + min(last, curr)
            n+=1
        return min(last, curr)  