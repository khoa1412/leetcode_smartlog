#
# @lc app=leetcode id=1470 lang=python3
#
# [1470] Shuffle the Array
#

# @lc code=start
class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        half = len(nums)//2
        nums1 = nums[half:]
        nums2 = nums[:half]
        i = 0 
        nums3 = []
        while i<half:
            nums3.append(nums2[i])
            nums3.append(nums1[i])
            i+=1
        return nums3
# @lc code=end

