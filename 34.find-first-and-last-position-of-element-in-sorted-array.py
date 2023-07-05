#
# @lc app=leetcode id=34 lang=python3
#
# [34] Find First and Last Position of Element in Sorted Array
#

# @lc code=start
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        rever_nums = list(reversed(nums))
        print(type(rever_nums))
        if target not in nums:
            return [-1, -1]
        else:
            start = nums.index(target)
            end = rever_nums.index(target)
            end = len(nums) - 1 - end
        return [start, end]
        
# @lc code=end

