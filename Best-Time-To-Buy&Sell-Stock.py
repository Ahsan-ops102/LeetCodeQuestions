class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = prices[0]
        max_profit = 0

        for i in range(1,len(prices)):
            if min_price > prices[i]:
                min_price = prices[i]
            
            diff = prices[i] - min_price
            if diff > max_profit:
                max_profit = diff
        return max_profit