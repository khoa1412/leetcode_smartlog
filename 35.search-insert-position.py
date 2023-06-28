#
# @lc app=leetcode id=35 lang=python3
#
# [35] Search Insert Position
#

# @lc code=start
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        i=0
        if target in nums:
            return nums.index(target)
        else:
            target_list = [target]
            nums.extend(target_list)
            nums.sort()
            return nums.index(target)
# @lc code=end

