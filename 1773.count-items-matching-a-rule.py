#
# @lc app=leetcode id=1773 lang=python3
#
# [1773] Count Items Matching a Rule
#

# @lc code=start
class Solution:
    def countMatches(self, items: List[List[str]], ruleKey: str, ruleValue: str) -> int:
        keys = {'type': 0, 'color': 1, 'name': 2}
        c = 0
        index = keys[ruleKey]
        for i in items:
            if i[index] == ruleValue:
                c += 1
        return c  
# @lc code=end

