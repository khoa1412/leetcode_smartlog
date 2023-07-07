#
# @lc app=leetcode id=29 lang=python3
#
# [29] Divide Two Integers
#

# @lc code=start
class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        output = int(dividend/divisor)
        if output not in range(-2**31, 2**31):
            return 2**31 - 1 if output > 0 else -2**31
        else:
            return output 
# @lc code=end

