#
# @lc app=leetcode id=1588 lang=python3
#
# [1588] Sum of All Odd Length Subarrays
#

# @lc code=start
class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        n = len(arr)
        res = 0
        for l in range(1, n+1, 2):
            for i in range(n - l +1):
                res += sum(arr[i:i + l])
        return res
# @lc code=end

