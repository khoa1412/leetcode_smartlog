#
# @lc app=leetcode id=260 lang=python3
#
# [260] Single Number III
#

# @lc code=start
class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        output = []
        for ele in list(set(nums)):
            if nums.count(ele) == 1:
                output.append(ele)
        return output
# @lc code=end

