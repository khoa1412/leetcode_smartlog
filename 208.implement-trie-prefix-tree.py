#
# @lc app=leetcode id=208 lang=python3
#
# [208] Implement Trie (Prefix Tree)
#

# @lc code=start
class Trie:

    def __init__(self):
        self.first = []

    def insert(self, word: str) -> None:
        self.first.insert(0,word)

    def search(self, word: str) -> bool:
        return word in self.first

    def startsWith(self, prefix: str) -> bool:
        if len(self.first) ==0:
            return False
        for i in range(len(self.first)): 
            if prefix == self.first[i][0:len(prefix)]:
                return True
            else:
                continue
        return False

# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
# @lc code=end

