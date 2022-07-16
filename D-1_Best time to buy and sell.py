	
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        ans = 0
        minSoFar = prices[0]
        for i in range (1,len(prices)):
            profit = prices[i] - minSoFar
            if (profit>ans):
                ans = profit
            minSoFar = min(minSoFar,prices[i])
        return ans
