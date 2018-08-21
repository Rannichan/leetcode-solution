class Solution:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if len(prices) < 2:
            return 0
        profit = 0
        buy_price = prices[0]
        go_up = 0
        for date in range(1, len(prices)):
            if prices[date] < prices[date-1]:
                if go_up == 1:
                    # if the price go up on the date before and the price go down on this date
                    # we sell the stock and accumulate the profit
                    profit += sell_price - buy_price
                # if the price go down on this date, we always need to update the "buy_price"
                buy_price = prices[date]
                # set a flag to indicate the tendency of the price
                go_up = 0
            elif prices[date] > prices[date-1]:
                sell_price = prices[date]
                if date == len(prices)-1:
                    profit += sell_price - buy_price
                go_up = 1
            else:
                if date == len(prices)-1 and go_up == 1:
                    profit += sell_price - buy_price
        return profit

if __name__ == '__main__':
    prices = [1,9,6,9,1,7,1,1,5,9,9,9]
    s = Solution()
    print(s.maxProfit(prices))