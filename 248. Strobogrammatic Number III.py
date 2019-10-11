'''
Title     : 248. Strobogrammatic Number III ($$$)
Problem   : https://leetcode.com/problems/strobogrammatic-number-iii/description/
'''
'''
one obvious way is to generate all strobogrammatic numbers with len(low) <= length <= len(high) and then filter
the following solution generate strobogrammatic numbers while simultaneously enforcing the bound
Reference: https://github.com/kongpingfan/Leetcode-Premium/blob/master/note/248.%20Strobogrammatic-Number-III.md
'''
from copy import copy
class Solution:
    def strobogrammaticInRange(self, low: str, high: str)->int:
        if int(low) >= int(high): return 1
        if len(low) == len(high):
            res = list(filter(lambda n: low <= n <= high, self.findStrobogrammatic(len(low))))
        else:
            res = []
            for i in range(len(low), len(high)+1):
                if i == len(low):
                    res += list(filter(lambda n: low <= n, self.findStrobogrammatic(i)))
                elif i == len(high):
                    res += list(filter(lambda n: n <= high, self.findStrobogrammatic(i)))
                else:
                    res += self.findStrobogrammatic(i)
        return len(res)

    def findStrobogrammatic(self, n):   # just cut and paste the 247. solution
        s = ['0', '1', '8', '6', '9']
        d = {'0': '0', '1': '1', '6': '9', '8': '8', '9': '6'}
        res, tmp = [''], []
        if n == 0: return res
        mid = n // 2
        i = 0
        while i < mid:
            if i == 0:
                for k in s[1:]: tmp.append(k + d[k])
            else:
                for j in res:
                    for k in s: tmp.append(j[:i] + k + d[k] + j[i:])
            res = copy(tmp)
            tmp = []
            i += 1
        if n % 2 != 0:
            for j in res:
                for k in range(3): tmp.append(j[:i] + s[k] + j[i:])
            res = copy(tmp)
        return res