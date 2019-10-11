'''
Title     : 293. Flip Game ($$$)
Problem   : https://leetcode.com/problems/flip-game/
          : https://www.lintcode.com/problem/flip-game/description
'''
''' step-by-step for loop '''
class Solution:
    def generatePossibleNextMoves(self, s):
        res = []
        for i in range(len(s)):
            if s[i:i+2] == '++':
                res.append(s[:i] + '--' + s[i+2:])
        return res

''' use list comprehension to avoid for loop, ibid. '''
class Solution:
    def generatePossibleNextMoves(self, s):
        return [(s[:i] + '--' + s[i+2:]) for i in range(len(s)) if s[i:i+2]=='++']