class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0 
        min_price = prices[0]

        for p in prices:
            if p < min_price:
                min_price = p
            else:
                profit = p - min_price
                max_profit = max (max_profit, profit)
        return max_profit
        