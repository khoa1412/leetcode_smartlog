#
# @lc app=leetcode id=1528 lang=python3
#
# [1528] Shuffle String
#

# @lc code=start
class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        arr = list(zip(indices,s))
        arr.sort()
        letters = [ second for _,second in arr ]
        return ''.join(letters)
# @lc code=end

