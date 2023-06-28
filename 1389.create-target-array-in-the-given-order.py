#
# @lc app=leetcode id=1389 lang=python3
#
# [1389] Create Target Array in the Given Order
#

# @lc code=start
class Solution:
    def createTargetArray(self, nums: List[int], index: List[int]) -> List[int]:
        tar_arr = []
        i = 0
        while i < len(index):
            tar_arr.insert(index[i],nums[i])
            i+=1
        return tar_arr
# @lc code=end

