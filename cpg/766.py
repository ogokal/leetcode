
from typing import List


class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        mr = len(matrix)
        mc = len(matrix[0])
        r = mr - 1
        for rr in range(mr-1, -1, -1):
            cc = 0
            start = matrix[rr][cc]
            while rr < mr and cc < mc:
                if matrix[rr][cc] != start:
                    return False
                rr += 1
                cc += 1
        for cc in range(0, mc):
            rr = 0
            start = matrix[rr][cc]
            while rr < mr and cc < mc:
                if matrix[rr][cc] != start:
                    return False
                rr += 1
                cc += 1
        return True


print(Solution().isToeplitzMatrix([
    [11, 74, 0, 93],
    [40, 11, 74, 7]
]))
