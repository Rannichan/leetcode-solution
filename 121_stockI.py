class Solution:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if len(prices) < 2:
            return 0
        min_val = min(prices)
        min_idx = prices.index(min_val)
        max_val = max(prices)
        max_idx = prices.index(max_val)
        if min_idx == max_idx:
            # if prices doesn't change during the days, the max profit will be 0
            return 0
        elif min_idx < max_idx:
            # if minimum price emerges before maximum price, the max profit will be difference of them
            buy_date = min_idx
            sell_date = max_idx
            return prices[sell_date]-prices[buy_date]
        else:
            # if minimum price emerges after maximum price, there be 3 possible situations at most
            profits = []
            if min_idx < len(prices)-1:
                max_val_pos = max(prices[min_idx+1:])
                profit_1 = max_val_pos - min_val
                profits.append(profit_1)
            if max_idx > 0:
                min_val_pre = min(prices[:max_idx])
                profit_2 = max_val - min_val_pre
                profits.append(profit_2)
            if min_idx - max_idx > 1:
                profit_3 = self.maxProfit(prices[max_idx+1:min_idx])
                profits.append(profit_3)
            if profits:
                return max(profits)
            else:
                return 0