"""
Big idea: heap sort
"""

class Solution:
    def kSmallestPairs(self, nums1, nums2, k):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :type k: int
        :rtype: List[List[int]]
        """
        if len(nums1)*len(nums2) == 0:
            return []

        result = []
        # coordinate of the current pair
        current = [0, 0]
        # top left is the smallest
        result.append([nums1[0], nums2[0]])

        # use a 2-D table to record if a pair was picked before
        is_reached = [[0 for _ in range(len(nums1))] for _ in range(len(nums2))]
        is_reached[0][0] = 1

        for i in range(k - 1):
            current_sum = nums2[current[0]] + nums1[current[1]]
            next = [-1, -1]
            # pick a number larger than the sum of the largest pair
            next_sum = nums2[next[0]] + nums1[next[1]] + 1

            for m in range(current[0] + 1):
                for n in range(current[1] + 1, len(nums1)):
                    ur = [m, n]
                    if is_reached[ur[0]][ur[1]] == 1:
                        continue
                    ur_sum = nums2[ur[0]] + nums1[ur[1]]
                    if current_sum <= ur_sum < next_sum:
                        next = ur
                        next_sum = ur_sum

            for n in range(current[1] + 1):
                for m in range(current[0] + 1, len(nums2)):
                    ld = [m, n]
                    if is_reached[ld[0]][ld[1]] == 1:
                        continue
                    ld_sum = nums2[ld[0]] + nums1[ld[1]]
                    if current_sum <= ld_sum < next_sum:
                        next = ld
                        next_sum = ld_sum

            if next != [-1, -1]:
                result.append([nums1[next[1]], nums2[next[0]]])
                is_reached[next[0]][next[1]] = 1
                current = next

        return result

    def kSmallestPairs2(self, nums1, nums2, k):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :type k: int
        :rtype: List[List[int]]
        """
        import heapq
        ret = []
        if len(nums1) * len(nums2) > 0:
            queue = [(nums1[0] + nums2[0], (0, 0))]
            visited = {}
            while len(ret) < k and queue:
                _, (i, j) = heapq.heappop(queue)
                ret.append((nums1[i], nums2[j]))
                if j + 1 < len(nums2) and (i, j + 1) not in visited:
                    heapq.heappush(queue, (nums1[i] + nums2[j + 1], (i, j + 1)))
                    visited[(i, j + 1)] = 1
                if i + 1 < len(nums1) and (i + 1, j) not in visited:
                    heapq.heappush(queue, (nums1[i + 1] + nums2[j], (i + 1, j)))
                    visited[(i + 1, j)] = 1
        return ret


if __name__ == '__main__':
    s = Solution()
    nums1 = [1, 2, 4]
    nums2 = [-1, 1, 2]
    k = 10
    print(s.kSmallestPairs(nums1, nums2, k))
    print(s.kSmallestPairs2(nums1, nums2, k))

