class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        #Optimal Solution using TWO POINTERS
        l, r = 0, 1
        maxP = 0

        while r < len(prices):
            if prices[l] < prices[r]:
                profit = prices[r] - prices[l]
                maxP = max(maxP, profit)
            else:
                l = r
            r += 1
        return maxP
        
        
        
        #Brute force approach
        # res = 0
        
        # for i in range(len(prices)):
        #     buying = prices[i]

        #     for j in range(i+1, len(prices)):
        #         selling = prices[j]
        #         res = max(res, selling - buying)

        # return res

        