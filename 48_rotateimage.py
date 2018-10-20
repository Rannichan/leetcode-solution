class Solution:
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        for i in range(n):
            row_i = [matrix[i][col] for col in range(n)]
            col_i = [matrix[row][i] for row in range(n)]
            for j in range(n-i, n):
                matrix[i][j] = row_i[n-j-1]
            for j in range(n-i):
                matrix[i][j] = col_i[n-j-1]
            for k in range(i+1,n):
                matrix[k][i] = row_i[k]
            # print(i)
            # for item in matrix:
            #     print(item)


if __name__ == '__main__':
    m = [[1,2,3],[4,5,6,],[7,8,9]]
    # for item in m:
    #     print(item)
    S = Solution()
    S.rotate(m)
    for item in m:
        print(item)