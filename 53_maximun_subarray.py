class Solution:
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        leftmax = nums[0]
        result = nums[0]
        for i in range(1, len(nums)):
            leftmax = max(nums[i], leftmax+nums[i])
            result = max(leftmax, result)
        return result
