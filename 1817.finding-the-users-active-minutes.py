#
# @lc app=leetcode id=1817 lang=python3
#
# [1817] Finding the Users Active Minutes
#

# @lc code=start
class Solution:
    def findingUsersActiveMinutes(self, logs: List[List[int]], k: int) -> List[int]:
        l=list(map(int,"0"*k))
        d=dict()
        for i in logs:
            if(i[0] not in d.keys()):
                s=set()
                s.add(i[1])
                d[i[0]]=s
            else:
                s=d.get(i[0])
                s.add(i[1])
                d[i[0]]=s
        for x,y in d.items():
            l[len(y)-1]+=1
        return l
# @lc code=end

