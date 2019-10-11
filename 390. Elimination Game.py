'''
Title     : 390. Elimination Game
Problem   : https://leetcode.com/problems/elimination-game/description/
'''
''' Reference: https://leetcode.com/problems/elimination-game/discuss/148451/Easy-Python-3-solution-4-lines '''
class Solution:
    def lastRemaining(self, n: int) -> int:
        res = range(1, n+1)
        while len(res) > 1:
            res = res[1::2][::-1]
        return res[0]