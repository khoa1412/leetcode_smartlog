#
# @lc app=leetcode id=53 lang=python3
#
# [53] Maximum Subarray
#

# @lc code=start
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        dp = [0]*len(nums)
        for i, num in enumerate(nums):
            dp[i] = max(dp[i-1] + num, num)
        return max(dp)
# @lc code=end

