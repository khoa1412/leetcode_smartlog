#
# @lc app=leetcode id=1282 lang=python3
#
# [1282] Group the People Given the Group Size They Belong To
#

# @lc code=start
class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        set_arr = set(groupSizes)
        output = []
        for arr in set_arr:
            search = []
            for i in range(len(groupSizes)):
                if groupSizes[i] == arr:
                    search.append(i)
                    if len(search) % arr == 0:
                        output.append(search)
                        search = []
        return output
# @lc code=end

