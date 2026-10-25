class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l,r = 0, 0
        sellprice = 0
        for r in range(len(prices)):
            if prices[l] > prices[r]:
                l = r
            if r >= 1 and prices[r] > prices[r-1]:
                sellprice = max(prices[r] - prices[l], sellprice)
        return sellprice