#
# @lc app=leetcode id=49 lang=python3
#
# [49] Group Anagrams
#

# @lc code=start
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        temp = defaultdict(list)
        for ele in strs:
            temp[str(sorted(ele))].append(ele)
        res = sorted(temp.values())
        return res
# @lc code=end

