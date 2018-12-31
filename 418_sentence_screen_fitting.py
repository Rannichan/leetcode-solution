"""
Given a rows x cols screen and a sentence represented by a list of words, find how many times the given sentence can be fitted on the screen.

Note:
    A word cannot be split into two lines.
    The order of words in the sentence must remain unchanged.
    Two consecutive words in a line must be separated by a single space.
    Total words in the sentence won't exceed 100.
    Length of each word won't exceed 10.
    1 ≤ rows, cols ≤ 20,000.
"""

class Solution:
    def wordTyping(self, s, row, col):
        """

        :param s: list
        :param row: int
        :param col: int
        :return:
        """
        totalNum = 0
        cur_col = col
        lenOfSen = sum([len(word)+1 for word in s])
        lenOfPart = []
        l = -1
        for word  in s:
            l += len(word)+1
            lenOfPart.append(l)
        lenLeft = 0
        for i in row:
            n = (col - lenLeft)/lenOfSen
            totalNum += (n+1)
            colLeft = col - lenLeft - n*lenOfSen
            for j in range(len(lenOfPart)):
                if colLeft < lenOfPart[j]:
                    break
            lenLeft = lenOfPart[-1] - lenLeft[j]
        if lenLeft == 0:
            totalNum += 1
        return totalNum


