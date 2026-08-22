class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_buy_price = []
        max_profit = 0
        for i,price in enumerate(prices):
            buy_price = price;
            if (i == 0):
                min_price = price
            else :
                min_price = min(min_buy_price[i-1],price)
            
            min_buy_price.append(min_price)

            max_profit = max (price - min_buy_price[i],max_profit)
        return max_profit
        