#
# @lc app=leetcode id=1572 lang=python3
#
# [1572] Matrix Diagonal Sum
#

# @lc code=start
class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        n = len(mat)
        sum_dia = 0
        for i in range(n):
            sum_dia += mat[i][i] + mat[i][n-i-1]
        if n%2==1:
            sum_dia -= mat[n//2][n//2]
        return sum_dia
# @lc code=end

