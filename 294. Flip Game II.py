'''
Title     : 294. Flip Game II ($$$)
Problem   : https://leetcode.com/problems/flip-game-ii/
          : https://www.lintcode.com/problem/flip-game-ii/description
'''
'''
recursive solution
Reference: http://www.voidcn.com/article/p-fpgsbray-zo.html
'''
class Solution:
    def canWin(self, s):
        if len(s) < 2: return False
        for i in range(len(s)-1):
            if s[i:i+2]=='++' and not self.canWin(s[:i]+'-'+s[i+2:]):   # self.canWin(s[:i]+'-'+s[i+2:]) == False means the opponent can NOT win
                return True
        return False