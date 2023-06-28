#
# @lc app=leetcode id=2535 lang=python3
#
# [2535] Difference Between Element Sum and Digit Sum of an Array
#

# @lc code=start
class Solution:
    def differenceOfSum(self, nums: List[int]) -> int:
        ele_nums=0
        for ele in nums:
            ele_nums +=ele
        nums1 = []
        for i in range(len(nums)):
            new = [int(x) for x in str(nums[i])]
            nums1.extend(new)
        dig_nums =0
        for nums1_ele in nums1:
            dig_nums += nums1_ele
        absolute_diff = abs(ele_nums - dig_nums)
        return absolute_diff  
# @lc code=end

