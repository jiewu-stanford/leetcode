'''
Title     : 320. Generalized Abbreviation ($$$)
Problem   : https://leetcode.com/problems/generalized-abbreviation/
          : https://www.lintcode.com/problem/generalized-abbreviation/description
'''
'''
recursive solution
Reference: https://github.com/kamyu104/LeetCode-Solutions/blob/master/Python/generalized-abbreviation.py
'''
class Solution:
    def generateAbbreviations(self, word: str) -> List[str]:
        if not word: return []
        res = []
        self.helper(word, 0, [], res)
        return res

    def helper(self, word, startindex, acc, res):
        if startindex == len(word):
            res.append(''.join(acc))
            return
        else:
            acc.append(word[startindex])
            self.helper(word, startindex+1, acc, res)
            acc.pop()
            if not acc or not acc[-1][-1].isdigit():
                for i in range(1, len(word)-startindex+1):
                    acc.append(str(i))
                    self.helper(word, startindex+i, acc, res)
                    acc.pop()