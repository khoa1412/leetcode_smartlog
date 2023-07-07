#
# @lc app=leetcode id=73 lang=python3
#
# [73] Set Matrix Zeroes
#

# @lc code=start
class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        def detectZeroes(input: List[List[int]]):
            posi = []
            for i in range(len(input)):
                for j in range(len(input[0])):
                    if input[i][j] == 0:
                        posi.append([i,j])
            return posi
        index = detectZeroes(matrix)
        for m, n in index:
            matrix[m] = [0]*len(matrix[0])
            for k in range(len(matrix)):
                matrix[k][n] = 0
# @lc code=end

