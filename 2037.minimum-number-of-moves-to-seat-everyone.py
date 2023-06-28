#
# @lc app=leetcode id=2037 lang=python3
#
# [2037] Minimum Number of Moves to Seat Everyone
#

# @lc code=start
class Solution:
    def minMovesToSeat(self, seats: List[int], students: List[int]) -> int:
        seats = sorted(seats)
        students = sorted(students)
        moves = 0
        for x in range(0,len(seats)):
            moves += abs(seats[x]-students[x])
        return moves
# @lc code=end

