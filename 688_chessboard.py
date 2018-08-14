# The given problem is a Markov process, therefore it is easy to form the idea below.
# Form a initial state (described by r & c), after K-times moving, we will get a final state.
# Each state is a possibility distribution over the whole chessboard.
# We only need to maintain a 2D list to store the state after each moving.
# At last, we sum the final distribution to get the result.
class Solution:
    def knightProbability(self, N, K, r, c):
        """
        :type N: int
        :type K: int
        :type r: int
        :type c: int
        :rtype: float
        """
        board = [[0 for _ in range(N)] for _ in range(N)]
        board[r][c] = 1
        # for line in board:
        #     print(line)
        for _ in range(K):
            board = self.move(board)
            # for line in board:
            #     print(line)
        return sum([sum(raw) for raw in board])

    def move(self, board):
        N = len(board)
        new_board = [[0 for _ in range(N)] for _ in range(N)]
        for raw in range(N):
            for col in range(N):
                possible_move = [
                    [raw - 2, col - 1],
                    [raw - 2, col + 1],
                    [raw + 2, col - 1],
                    [raw + 2, col + 1],
                    [raw - 1, col - 2],
                    [raw - 1, col + 2],
                    [raw + 1, col - 2],
                    [raw + 1, col + 2]
                ]
                for item in possible_move:
                    if 0 <= item[0] <= N - 1 and 0 <= item[1] <= N - 1:
                        new_board[raw][col] += board[item[0]][item[1]] / 8.0
        return new_board

if __name__ == '__main__':
    N, k, r, c = 3, 2, 0, 0
    s = Solution()
    s.knightProbability(N, k, r, c)