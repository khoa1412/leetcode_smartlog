#
# @lc app=leetcode id=1769 lang=python3
#
# [1769] Minimum Number of Operations to Move All Balls to Each Box
#

# @lc code=start
class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        pos = [x for x in range(len(boxes)) if boxes[x] == "1"]
        print(pos)
        output = []
        for i in range(len(boxes)):
            moves = 0
            for j in pos:
                moves += abs(j-i)
            output.append(moves)
        return output
# @lc code=end

