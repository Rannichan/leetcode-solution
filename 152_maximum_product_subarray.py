class Solution:
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        pre_leftmax = nums[0]
        pre_leftmin = nums[0]
        result = nums[0]
        for i in range(1, len(nums)):
            leftmax = max(nums[i], pre_leftmax*nums[i], pre_leftmin*nums[i])
            leftmin = min(nums[i], pre_leftmax * nums[i], pre_leftmin * nums[i])
            pre_leftmax = leftmax
            pre_leftmin = leftmin
            result = max(result, leftmax)
        return result