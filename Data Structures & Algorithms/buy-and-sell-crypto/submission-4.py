class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # result = 0
        # for i in range(len(prices)):
        #     for j in range(i, len(prices)):
        #         if prices[j] - prices[i] > result and prices[j] > prices[i]:
        #             result = prices[j] - prices[i]
        # return result
        l, r = 0, 1
        result = 0

        while r < len(prices):
            if prices[l] < prices[r]:
                diff = prices[r] - prices[l]
                if diff > result:
                    result = diff
                r += 1
            else:
                l = r
                r += 1
        return result