'''
Title     : 246. Strobogrammatic Number ($$$)
Problem   : https://leetcode.com/problems/strobogrammatic-number/description/
          : https://www.lintcode.com/problem/strobogrammatic-number/description
'''
'''
construct from the 2-digit building block of strobogrammatic numbers
Reference: http://www.voidcn.com/article/p-dqtajpmz-qp.html
'''
class Solution:
    def isStrobogrammatic(self, num):
        if not num: return False
        for i in range(len(num)//2 + 1):
            if num[i] + num[-i-1] not in '696001188': return False
        return True   # return all(num[i] + num[~i] in '696 00 11 88' for i in range(len(num)//2+1))

''' Reference: https://blog.csdn.net/danspace1/article/details/88944960 '''
class Solution(object):
    def isStrobogrammatic(self, num):
        d = {'0':'0','1':'1','6':'9','8':'8','9':'6'}
        res = ''
        for n in num:
            if n not in d: return False
            res += d[n]
        return res[::-1] == num   # not only should the digits be 0, 1, 6, 8, 9 whose mirror images are valid digits but also their positions be mirror symmetric