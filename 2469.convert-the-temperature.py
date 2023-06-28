#
# @lc app=leetcode id=2469 lang=python3
#
# [2469] Convert the Temperature
#

# @lc code=start
class Solution:
    def convertTemperature(self, celsius: float) -> List[float]:
        kelvin, fahr = celsius +273.15,celsius*1.80+32.00
        return [kelvin,fahr]
# @lc code=end

