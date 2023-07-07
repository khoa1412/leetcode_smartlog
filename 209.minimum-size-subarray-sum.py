#
# @lc app=leetcode id=209 lang=python3
#
# [209] Minimum Size Subarray Sum
#

# @lc code=start
class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        leng_sec = maxsize
        sum_sub, posi = 0, 0
        for i in range(len(nums)):
            sum_sub += nums[i]
            while sum_sub >= target:
                leng_sec = min(leng_sec, i - posi + 1)
                sum_sub -= nums[posi]
                posi += 1
        return leng_sec if leng_sec != maxsize else 0
# @lc code=end

