'''
Title     : 247. Strobogrammatic Number II ($$$)
Problem   : https://leetcode.com/problems/strobogrammatic-number-ii/description/
          : https://www.lintcode.com/problem/strobogrammatic-number-ii/description
'''
'''
recursive generator, decomposition in the form of 1-digit + ... + 1-digit
Reference: https://www.cnblogs.com/lightwindy/p/8491311.html
'''
class Solution:
    def findStrobogrammatic(self, n):
        return self.helper(n, n)

    def helper(self, n, k):
        if k == 0: return ['']
        if k == 1: return ['0','1','8']
        middles = self.helper(n, k-2)
        res = []
        for middle in middles:
            if n != k: res.append('0' + middle + '0')   # padding '0' is disallowed only when k = n
            res.append('8' + middle + '8')
            res.append('1' + middle + '1')
            res.append('6' + middle + '9')
            res.append('9' + middle + '6')
        return res
'''
iterative solution carrying out explicitly the padding construction in the recursive solution
Reference: http://www.voidcn.com/article/p-rltfcrmu-zo.html
'''
from copy import copy   # we will use hard copy instead of soft copy
class Solution:
    def findStrobogrammatic(self, n):
        s = ['0', '1', '8', '6', '9']
        d = {'0': '0', '1': '1', '6': '9', '8': '8', '9': '6'}
        res, tmp = [''], []
        if n == 0: return res

        mid = n // 2
        i = 0
        while i < mid:
            if i == 0:
                for k in s[1:]: tmp.append(k + d[k])   # starting from 2-digit strobogrammatic numbers excluding '00'
            else:
                for j in res:
                    for k in s: tmp.append(j[:i] + k + d[k] + j[i:])
            res = copy(tmp)
            tmp = []
            i += 1
            
        if n % 2 != 0:
            for j in res:
                for k in range(3): tmp.append(j[:i] + s[k] + j[i:])   # sandwiching a strobogrammatic digit to go from even-length to odd-length
            res = copy(tmp)
        
        return res