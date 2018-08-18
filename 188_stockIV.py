class Solution:
    def maxProfit(self, k, prices):
        """
        :type k: int
        :type prices: List[int]
        :rtype: int
        """

    def maxTran(self, prices):
        minval = min(prices)
        minidx = prices.index(minval)
        maxval = max(prices)
        maxidx = prices.index(maxval)
        if minidx == maxidx:
            return -1
        elif minidx < maxidx:
            return [minidx, maxidx]
        else:
            minval2 = min(prices[:maxidx])
            profits1 = maxval - minval2
            maxval2 = max(prices[minidx+1:])
            profits2 = maxval2 - minval
            if profits1 >= profits2:
                return [prices.index(minval2), maxidx]
            else:
                return [minidx, prices.index(maxval2)]
