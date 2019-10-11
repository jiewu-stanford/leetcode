'''
Title     : 38. Count and Say
Problem   : https://leetcode.com/problems/count-and-say/
'''
''' Reference: https://leetcode.com/problems/count-and-say/discuss/172315/Python-solution '''
class Solution:
    def countAndSay(self, n: int) -> str:
        res = '1'
        for _ in range(n-1):
            letter, say, count = res[0], '', 0
            for c in res:
                if c == letter:
                    count += 1
                else:
                    say += str(count) + letter
                    letter = c
                    count = 1
            say += str(count) + letter
            res = say
        return res

''' Reference: https://leetcode.com/problems/count-and-say/discuss/15999/4-5-lines-Python-solutions '''
import itertools
class Solution:
    def countAndSay(self, n: int) -> str:
        res = '1'
        for _ in range(n-1):
            say = ''
            for letter, group in itertools.groupby(res):
                count = len(list(group))
                say += str(count) + letter   # say += '%i%s' % (count, letter)
            res = say
        return res