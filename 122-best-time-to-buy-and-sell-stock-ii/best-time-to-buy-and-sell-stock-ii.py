class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_prof = 0
        minimum = float('inf')
        for price in prices:
            minimum = min(minimum, price)
            profit = price - minimum
            if profit > 0:
                max_prof += profit
                minimum = price
        return max_prof