class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_prof = 0
        min_price = float('inf')
        for each in prices:
            min_price = min(min_price, each)
            potential = each - min_price
            if potential > max_prof:
                max_prof = potential
        return max_prof


        