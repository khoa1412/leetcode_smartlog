#
# @lc app=leetcode id=2652 lang=python3
#
# [2652] Sum Multiples
#

# @lc code=start
class Solution:
    def sumOfMultiples(self, n: int) -> int:
        sum1 = 0
        for i in range(1, n+1):
            if i%3 == 0 or i%5==0 or i%7==0:
                sum1 +=i
        return sum1
# @lc code=end

