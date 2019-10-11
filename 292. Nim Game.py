'''
Title     : 292. Nim Game (XXX)
Problem   : https://leetcode.com/problems/nim-game/
'''
''' the problem illustrates why 4 is losing, apply the same argument to the mathematical induction step from 4K to 4(K+1) '''
class Solution:
    def canWinNim(self, n: int) -> bool:
        return n % 4 != 0