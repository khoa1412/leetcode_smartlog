#
# @lc app=leetcode id=2011 lang=python3
#
# [2011] Final Value of Variable After Performing Operations
#

# @lc code=start
class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        operate = {"++X":1,"X++":1,"--X":-1,"X--":-1}
        x = 0
        i = 0
        while i<len(operations):
            x += operate[operations[i]]
            i+=1
        return x
# @lc code=end

