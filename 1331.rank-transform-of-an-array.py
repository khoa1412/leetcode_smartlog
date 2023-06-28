#
# @lc app=leetcode id=1331 lang=python3
#
# [1331] Rank Transform of an Array
#

# @lc code=start
class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        rank = {}
        for i in sorted(arr):
            rank.setdefault(i, len(rank)+1)
        return map(rank.get,arr)
# @lc code=end

