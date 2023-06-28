#
# @lc app=leetcode id=804 lang=python3
#
# [804] Unique Morse Code Words
#

# @lc code=start
class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        MORSE = {"a":".-","b":"-...","c":"-.-.","d":"-..","e":".","f":"..-.","g":"--.","h":"....","i":"..","j":".---","k":"-.-","l":".-..","m":"--","n":"-.","o":"---","p":".--.","q":"--.-","r":".-.","s":"...","t":"-","u":"..-","v":"...-","w":".--","x":"-..-","y":"-.--","z":"--.."}
        new_list =[]
        string = ""
        for i in range(len(words)):
                for j in range(len(words[i])):
                        string +=(MORSE[words[i][j]])
                new_list.append(string)
                print(string)
                string =''
        print(new_list)        
        word_set = set(new_list)
        return len(word_set) 
# @lc code=end

