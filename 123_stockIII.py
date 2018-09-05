# Divide the price list into two successive lists,
# then use method in 121_stockI.py get the max profit in each list.
# At last, add them up.
# Up to now, we got the "max profit" under a way of dividing.
# To get the result, we only have to conduct a traversal over all ways of dividing and find the max of "max profits"
# This is the most simple and natural idea, but exceed time limit.
class Solution1:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if len(prices) < 2:
            return 0
        profits = []
        for i in range(len(prices)):
            profit =  self.maxProfitI(prices[:i]) + self.maxProfitI(prices[i:])
            profits.append(profit)
        return max(profits)

    def maxProfitI(self, prices):
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
                profit_3 = self.maxProfitI(prices[max_idx+1:min_idx])
                profits.append(profit_3)
            if profits:
                return max(profits)
            else:
                return 0


class Solution2(object):
    def maxProfit(self, prices):
        if len(prices) <= 1: return 0

        # O(n) counting from left, find the max gain up to each day (not ending at each day)
        left = [0] * len(prices)
        curmin = prices[0]
        for i in range(1, len(prices)):
            curmin = min(curmin, prices[i])
            left[i] = max(prices[i] - curmin, left[i - 1])

        # O(n) counting from right
        right = [0] * len(prices)
        curmax = prices[-1]
        for i in range(len(prices) - 2, -1, -1):
            curmax = max(curmax, prices[i])
            right[i] = max(curmax - prices[i], right[i + 1])

        # O(n)
        max2t = 0
        for i in range(len(prices)):
            max2t = max(max2t, left[i] + right[i])
        return max2t

if __name__ == '__main__':
    prices = [8,3,6,2,8,8,8,4,2,0,7,2,9,4,9]
    s1 = Solution2()
    print(s1.maxProfit(prices))