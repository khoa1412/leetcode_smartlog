#
# @lc app=leetcode id=50 lang=python3
#
# [50] Pow(x, n)
#

# @lc code=start
class Solution:
    def myPow(self, x: float, n: int) -> float:
        output = 1
        temp = x
        if n >= 0:
            while n>0:
                if n%2 != 0:
                    output *= temp
                n = n // 2
                temp *= temp
            return output
        else:
            n = -n
            while n :
                if n%2 != 0:
                    output /= temp
                n = n // 2
                temp *= temp
            return output
# @lc code=end

