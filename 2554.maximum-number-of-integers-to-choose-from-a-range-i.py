#
# @lc app=leetcode id=2554 lang=python3
#
# [2554] Maximum Number of Integers to Choose From a Range I
#

# @lc code=start
class Solution:
    def maxCount(self, banned: List[int], n: int, maxSum: int) -> int:
        cnt = 0
        total = 0
        banned = set(banned)
        
        for i in range(1,n+1):
            if i not in banned and maxSum>=total+i:
                cnt+=1
                total+=i
        return cnt
# @lc code=end

