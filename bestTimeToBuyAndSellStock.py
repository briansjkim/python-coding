class Solution(object):
    def maxProfit(self, prices):
        max_profit = 0

        lowest_price = prices[0]
        for price in prices:
            if lowest_price > price:
                lowest_price = price
            else:
                max_profit = max(max_profit, price - lowest_price)
        return max_profit

# Don't need to use two pointers for this
