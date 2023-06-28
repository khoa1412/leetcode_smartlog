#
# @lc app=leetcode id=66 lang=python3
#
# [66] Plus One
#

# @lc code=start
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        s = [str(integer) for integer in digits]
        a_string = "".join(s)
        res = int(a_string)
        res+=1
        output = [int(x) for x in str(res)]
        return output
        
# @lc code=end

