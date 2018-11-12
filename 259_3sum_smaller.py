"""
Given an array of n integers nums and a target, find the number of index triplets i, j, k with 0 <= i < j < k < n that
satisfy the condition nums[i] + nums[j] + nums[k] < target.

For example, given nums = [-2, 0, 1, 3], and target = 2.

Return 2. Because there are two triplets which sums are less than 2:
[-2, 0, 1]
[-2, 0, 3]
Follow up:

Could you solve it in O(n2) runtime?
"""


class Solution(object):
    def threeSumSmaller(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        numbers = nums
        if len(numbers) < 3:
            return 0
        numbers.sort()
        result = 0
        for idx, num in enumerate(numbers):
            t = target - num
            #only start with afterward elements
            twoSumResults = self.twoSum(numbers[idx+1:], t)
            result += twoSumResults
        return result

    def twoSum(self, numbers, target):
        # need to find all combinations now
        if len(numbers) < 2:
            return 0
        result = 0
        start, end = 0, len(numbers) -1
        while start < end:
            while end > start and numbers[start] + numbers[end] >= target:
                end -= 1
            if start < end:
                result += end - start
                start += 1
            else:
                break

        return result