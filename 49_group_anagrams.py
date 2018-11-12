class Solution:
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        # from collections import Counter
        search_table = {}
        for str in strs:
            vec = tuple(sorted(str))
            if vec in search_table:
                search_table[vec].append(str)
            else:
                search_table[vec] = [str]
        return list(search_table.values())


if __name__ == '__main__':
    s = ["",""]
    S = Solution()
    print(S.groupAnagrams(s))