#
# @lc app=leetcode id=1732 lang=python3
#
# [1732] Find the Highest Altitude
#

# @lc code=start
class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        current_Altitude = 0
        max_Altitude = 0
        for alti in gain:
            current_Altitude += alti
            max_Altitude = max(current_Altitude, max_Altitude)
        return max_Altitude
# @lc code=end

