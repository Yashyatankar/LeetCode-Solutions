class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if not prices:
            return 0

        min_profit = prices[0]
        max_profit = 0

        for price in prices[1:]:

            if price < min_profit:

                min_profit = price

            elif price - min_profit > max_profit:

                max_profit = price - min_profit
        
        return max_profit