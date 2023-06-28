#
# @lc app=leetcode id=2225 lang=python3
#
# [2225] Find Players With Zero or One Losses
#

# @lc code=start
class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        winner, loser, table = [],[],{}
        result = []
        for win, lose in matches:
            table[win] = table.get(win, 0)
            table[lose] = table.get(lose, 0)+1
        print(table)
        for item in table:
            # print()
            record = table.get(item)
            if record == 0:
                winner.append(item)
            if record == 1:     
                loser.append(item)
        result.append(sorted(winner))
        result.append(sorted(loser))

        return result
# @lc code=end

