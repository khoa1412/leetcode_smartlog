#
# @lc app=leetcode id=338 lang=python3
#
# [338] Counting Bits
#

# @lc code=start
class Solution:
    def countBits(self, n: int) -> List[int]:
        l = []
        for i in range(n+1):
            stream = str(bin(i))
            times = stream.count('1')
            l.append(times)
        return l
# @lc code=end

