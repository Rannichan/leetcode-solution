class Solution:
    def findMaximumXOR(self, nums):
        """
        Solution 1 -- time limit exceeded
        First, find the longest "num"s in binary form.
        Second, set their last "masklen" digits into 1 and then find the largest one.
        This one must be chose to get largest XOR result.
        At last, travel the "nums" to find the pair having max XOR result within O(N) time limit
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 1:
            return 0

        maxlen = -1  # max length
        maxlen2 = -1  # second max length
        maxnums = []
        for num in nums:
            num_ = str(bin(num))[2:]
            length = len(num_)
            if length == maxlen:
                maxnums.append(num)
            elif length > maxlen:
                maxnums = [num]
                maxlen2 = maxlen
                maxlen = length
            else:
                if length > maxlen2:
                    maxlen2 = length
        # print(maxlen)
        # print(maxlen2)
        if maxlen2 == -1:
            cands = maxnums
        else:
            masklen = maxlen2  # 2nd max length
            cands = [int(x/(2**masklen)) for x in maxnums]  # use mask to remove the difference in last masklen binary digits
        maxcand = max(cands)  # get the max candidate
        result = -1
        for cand, num in zip(cands, maxnums):
            if cand == maxcand:
                for x in nums:
                    if num^x > result:
                        result = num^x
        return result


class Solution2:
    def findMaximumXOR(self, nums):
        pass


if __name__ == '__main__':
    nums = [8, 10, 2]
    s = Solution()
    print(s.findMaximumXOR(nums))