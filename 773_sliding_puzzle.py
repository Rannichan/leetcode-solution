"""
On a 2x3 board, there are 5 tiles represented by the integers 1 through 5, and an empty square represented by 0.

A move consists of choosing 0 and a 4-directionally adjacent number and swapping it.

The state of the board is solved if and only if the board is [[1,2,3],[4,5,0]].

Given a puzzle board, return the least number of moves required so that the state of the board is solved. If it is impossible for the state of the board to be solved, return -1.
"""
import copy


class Solution:
    def slidingPuzzle(self, board):
        """
        :type board: List[List[int]]
        :rtype: int
        """
        queue = [board]
        visited = []
        depth = 0
        while True:
            new_queue = []
            while queue:
                cur = queue.pop(0)
                visited.append(cur)
                if cur == [[1, 2, 3], [4, 5, 0]]:
                    return(depth)
                if 0 in cur[0]:
                    zero_x = 0
                    zero_y = cur[0].index(0)
                else:
                    zero_x = 1
                    zero_y = cur[1].index(0)
                next1 = copy.deepcopy(cur)
                next1[0][zero_y] = cur[1][zero_y]
                next1[1][zero_y] = cur[0][zero_y]
                if next1 not in visited:
                    new_queue.append(next1)
                if 1 <= zero_y:
                    next2 = copy.deepcopy(cur)
                    next2[zero_x][zero_y] = cur[zero_x][zero_y - 1]
                    next2[zero_x][zero_y - 1] = cur[zero_x][zero_y]
                    if next2 not in visited:
                        new_queue.append(next2)
                if zero_y <= 1:
                    next3 = copy.deepcopy(cur)
                    next3[zero_x][zero_y] = cur[zero_x][zero_y + 1]
                    next3[zero_x][zero_y + 1] = cur[zero_x][zero_y]
                    if next3 not in visited:
                        new_queue.append(next3)
            if new_queue:
                depth += 1
                queue.extend(new_queue)
            else:
                return(-1)