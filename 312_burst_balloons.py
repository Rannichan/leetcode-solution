class Solution(object):
    def maxCoins(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums = [1] + nums + [1]
        n = len(nums)
        dp = [[0] * n for _ in range(n)]

        def calculate(i, j):
            # calculate max score after eliminate element of index from i+1 to j-1
            if dp[i][j] or j == i + 1: # in memory or gap < 2, dp[i][i+1]=0
                return dp[i][j]
            coins = 0
            for k in range(i+1, j): # find the last balloon
                coins = max(coins, nums[i] * nums[k] * nums[j] + calculate(i, k) + calculate(k, j))
            dp[i][j] = coins
            return coins

        return calculate(0, n-1)


class MySolution:
    def maxCoins(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums_expand = [1] + nums + [1]
        max_coins = self.maxScore(nums_expand)
        return max_coins

    def maxScore(self, nums_expand):
        if len(nums_expand) == 2:
            return 0
        max_score = -float('Inf')
        last_num = nums_expand[1]
        for i in range(1, len(nums_expand) - 1):
            left_score = self.maxScore(nums_expand[:i + 1])
            right_score = self.maxScore(nums_expand[i:])
            current_score = nums_expand[0] * nums_expand[i] * nums_expand[-1]
            total_score = current_score + left_score + right_score
            if total_score > max_score:
                max_score = total_score
                last_num = nums_expand[i]
        return max_score


# really similar to the CKY algorithm in POS tagging problem
class Solution2(object):
    def maxCoins(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums = [1] + nums + [1]  # build the complete array
        n = len(nums)
        dp = [[0] * n for _ in range(n)]

        for gap in range(2, n):
            for i in range(n - gap):
                j = i + gap
                for k in range(i + 1, j):
                    dp[i][j] = max(dp[i][j], nums[i] * nums[k] * nums[j] + dp[i][k] + dp[k][j])
        return dp[0][n - 1]