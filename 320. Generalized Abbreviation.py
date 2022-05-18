'''
Title     : 320. Generalized Abbreviation ($$$)
Problem   : https://leetcode.com/problems/generalized-abbreviation/
          : https://www.lintcode.com/problem/generalized-abbreviation/description
'''
class Solution:
    def generateAbbreviations(self, word: str) -> List[str]:
        def dfs(ind, word):
            res.append(word)
            if ind >= len(word):
                return
            for n in range(1,len(word)+1):
                for i in range(ind, len(word)-n+1):
                    newword = word[:i] + str(n) + word[i+n:]
                    nextind = i + len(str(n)) + 1
                    dfs(nextind, newword)

        res = []
        dfs(0, word)
        return res