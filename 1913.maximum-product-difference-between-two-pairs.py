#
# @lc app=leetcode id=1913 lang=python3
#
# [1913] Maximum Product Difference Between Two Pairs
#

# @lc code=start
class Solution:
    def maxProductDifference(self, nums: List[int]) -> int:
        nums1 = sorted(nums, reverse = True)
        nums2 = sorted(nums)
        largest,smallest =1,1
        for i in range(2):
            largest *= nums1[i]
            smallest *= nums2[i]
        return largest - smallest
# @lc code=end

