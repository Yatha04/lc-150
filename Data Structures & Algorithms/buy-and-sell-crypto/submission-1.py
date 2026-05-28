class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profitMax = 0
        window = []
        left = 0
        right = 0

        for right in range(len(prices)):

            if (prices[right] < prices[left]):
                left = right
            profit = prices[right] - prices[left]
            profitMax = max(profit, profitMax)
        
        return profitMax
