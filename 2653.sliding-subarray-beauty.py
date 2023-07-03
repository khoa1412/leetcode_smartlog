#
# @lc app=leetcode id=2653 lang=python3
#
# [2653] Sliding Subarray Beauty
#

# @lc code=start
from sortedcontainers import SortedList
class Solution:
    def getSubarrayBeauty(self, nums: List[int], k: int, x: int) -> List[int]:
        a=SortedList([])
        ans=[]
        for ele in range(k):
            a.add(nums[ele])
        for i in range(k,len(nums)):
            if x<=len(a) and a[x-1]<0:
                ans.append(a[x-1])
            else:
                ans.append(0)
            a.remove(nums[i-k])
            a.add(nums[i])
        if x<=len(a) and a[x-1]<0:
                ans.append(a[x-1])
        else:
            ans.append(0)
        return ans
            
# @lc code=end

