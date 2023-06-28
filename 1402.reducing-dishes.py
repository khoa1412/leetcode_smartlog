#
# @lc app=leetcode id=1402 lang=python3
#
# [1402] Reducing Dishes
#

# @lc code=start
class Solution:
    def maxSatisfaction(self, satisfaction: List[int]) -> int:
        rs = 0
        list_index =  list(range(1, len(satisfaction)+1))
        satisfaction = sorted(satisfaction)

        for index,item in enumerate(satisfaction):
            check_sum = sum(x * y for x, y in zip(satisfaction[-index-1:], list_index[:index+1]))

            if(check_sum > rs):
                rs = check_sum
            else:
                break
        return rs
        
# @lc code=end

