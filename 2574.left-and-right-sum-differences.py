#
# @lc app=leetcode id=2574 lang=python3
#
# [2574] Left and Right Sum Differences
#

# @lc code=start
class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        ans=[0]
        for i in nums: ans+=[ans[-1]+i]
        a=[]
        for i in range(1,len(ans)):
            a+=[abs(ans[-1]-ans[i]-ans[i-1])]   
        return a
# @lc code=end

