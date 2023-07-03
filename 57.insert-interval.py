#
# @lc app=leetcode id=57 lang=python3
#
# [57] Insert Interval
#

# @lc code=start
class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        output = []
        for interval in intervals:
            if interval[1] < newInterval[0]:
                output.append(interval)
            elif interval[0] > newInterval[1]:
                output.append(newInterval)
                newInterval = interval
            elif interval[1] >= newInterval[0] or interval[0] <= newInterval[1]:
                newInterval[0] = min(interval[0], newInterval[0]) 
                newInterval[1] = max(interval[1], newInterval[1])
        output.append(newInterval)
        return output
# @lc code=end

