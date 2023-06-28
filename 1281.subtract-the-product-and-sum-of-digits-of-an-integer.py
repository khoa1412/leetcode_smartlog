#
# @lc app=leetcode id=1281 lang=python3
#
# [1281] Subtract the Product and Sum of Digits of an Integer
#

# @lc code=start
class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        prod = 1
        sumd = 0
        for i in range(len(str(n))):
            res = n%10
            sumd += res
            prod *= res
            n = n//10
        return prod - sumd
# @lc code=end

