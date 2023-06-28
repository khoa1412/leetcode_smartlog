#
# @lc app=leetcode id=2656 lang=python3
#
# [2656] Maximum Sum With Exactly K Elements 
#

# @lc code=start
class Solution:
    def maximizeSum(self, nums: List[int], k: int) -> int:
        maxi_score = 0
        times=0
        while times < k:
            maxi = max(nums)
            pos = nums.index(maxi)
            nums[pos] = maxi +1
            maxi_score += maxi 
            times+=1
        return maxi_score
# @lc code=end

