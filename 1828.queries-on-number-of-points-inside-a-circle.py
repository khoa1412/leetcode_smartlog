#
# @lc app=leetcode id=1828 lang=python3
#
# [1828] Queries on Number of Points Inside a Circle
#

# @lc code=start
class Solution:
    def countPoints(self, points: List[List[int]], queries: List[List[int]]) -> List[int]:
        output=[]
        
        for circle in queries:
            count = 0
            for point in points:
                if sqrt((point[0]-circle[0])**2 + (point[1]-circle[1])**2) <= circle[2]:
                    count+=1
            output.append(count)
        return(output)
# @lc code=end

