#
# @lc app=leetcode id=1313 lang=python3
#
# [1313] Decompress Run-Length Encoded List
#

# @lc code=start
class Solution:
    def decompressRLElist(self, nums: List[int]) -> List[int]:
        output = []
        i=0
        while i<len(nums):
            for k in range(nums[i]):
                output.append(nums[i+1])
            i+=2
        return output
# @lc code=end

