class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res = 0
        for i in range(len(prices)):
            buy = prices[i]
            profit = 0
            for j in range(i+1, len(prices)):
                if prices[j] > buy:
                    profit = max(profit, (prices[j] - buy))
            res = max(profit, res)
        return res 
