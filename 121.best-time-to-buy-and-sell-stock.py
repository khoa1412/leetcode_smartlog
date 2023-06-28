#
# @lc app=leetcode id=121 lang=python3
#
# [121] Best Time to Buy and Sell Stock
#

# @lc code=start
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        min_purchase = prices[0]
        for i in range(1, len(prices)):
            max_profit = max(max_profit, prices[i] - min_purchase)
            min_purchase = min(min_purchase, prices[i])
        return max_profit
# @lc code=end

