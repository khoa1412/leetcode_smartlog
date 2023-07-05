#
# @lc app=leetcode id=164 lang=python3
#
# [164] Maximum Gap
#

# @lc code=start
class Solution:
    def maximumGap(self, nums: List[int]) -> int:
        nums[::] = sorted(nums)
        max_diff = float("-inf")
        if len(nums) < 2:
            return 0
        else:
            for i in range(len(nums)-1):
                x = nums[i+1] - nums[i]
                if max_diff < x:
                    max_diff = x
        return max_diff
# @lc code=end

