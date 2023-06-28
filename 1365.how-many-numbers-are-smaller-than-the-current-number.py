#
# @lc app=leetcode id=1365 lang=python3
#
# [1365] How Many Numbers Are Smaller Than the Current Number
#

# @lc code=start
class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        temp = sorted(nums)
        mapping = {}
        result = []
        for i in range(len(temp)):
                if temp[i] not in mapping:
                        mapping[temp[i]] = i
        for i in range(len(nums)):
                result.append(mapping[nums[i]])
        return result
# @lc code=end

