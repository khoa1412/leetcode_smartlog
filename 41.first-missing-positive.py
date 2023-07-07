#
# @lc app=leetcode id=41 lang=python3
#
# [41] First Missing Positive
#

# @lc code=start
class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        unique = set(nums)
        i = 1
        while i in unique:
            i +=1
        return i

# @lc code=end

