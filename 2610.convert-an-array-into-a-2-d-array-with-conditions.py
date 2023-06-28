#
# @lc app=leetcode id=2610 lang=python3
#
# [2610] Convert an Array Into a 2D Array With Conditions
#

# @lc code=start
class Solution:
    def findMatrix(self, nums: List[int]) -> List[List[int]]:
        nums.sort(reverse=True)
        rows = []
        for num in nums:
            for row in rows: 
                if num not in row:
                    row.append(num)
                    break
            else:
                rows.append([num])
        return rows
# @lc code=end

