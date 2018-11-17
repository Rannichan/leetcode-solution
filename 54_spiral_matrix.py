"""
Given a matrix of m x n elements (m rows, n columns), return all elements of the matrix in spiral order.
"""


class Solution:
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        result = []
        height = len(matrix)
        if height == 0:
            return []
        else:
            width = len(matrix[0])
        if height == 1:
            return matrix[0]
        if width == 1:
            return [line[0] for line in matrix]

        for i in range(width):
            result.append(matrix[0][i])
        for i in range(1, height - 1):
            result.append(matrix[i][-1])
        for i in range(width):
            result.append(matrix[-1][width - i - 1])
        for i in range(1, height - 1):
            result.append(matrix[-i - 1][0])
        new_matrix = [line[1:-1] for line in matrix[1:-1] if len(line[1:-1]) != 0]
        result.extend(self.spiralOrder(new_matrix))
        return result