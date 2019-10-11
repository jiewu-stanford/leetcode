'''
Title     : 299. Bulls and Cows
Problem   : https://leetcode.com/problems/bulls-and-cows/description/
'''
'''
easy to understand two-pass iterative solution
Reference: https://leetcode.com/problems/bulls-and-cows/discuss/74775/PYTHON-dict-solution
'''
class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        d = {}
        bull, cow = 0, 0
        for i, s in enumerate(secret):
            if guess[i] == s:
                bull += 1
            else:
                d[s] = d.get(s,0) + 1
        for i, s in enumerate(secret):
            if (guess[i] != s) & (d.get(guess[i],0) != 0):
                cow += 1
                d[guess[i]] -= 1
        return str(bull) + 'A' + str(cow) + 'B'
'''
use zip() and Counter() to compare all at once, faster but less comprehensible
Reference: https://leetcode.com/problems/bulls-and-cows/discuss/74616/3-lines-in-Python
'''
import collections
class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        A = sum(a==b for a,b in zip(secret, guess))
        B = collections.Counter(secret) & collections.Counter(guess)
        return '%dA%dB' % (A, sum(B.values())-A)