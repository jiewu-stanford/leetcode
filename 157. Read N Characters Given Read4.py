'''
Title     : 157. Read N Characters Given Read4 ($$$)
Problem   : https://leetcode.com/problems/read-n-characters-given-read4/
'''
''' Reference: https://github.com/criszhou/LeetCode-Python/blob/master/157.%20Read%20N%20Characters%20Given%20Read4.py '''
class Reader:
    def read4(self, buf): pass

class Solution:
    def read(self, buf, n):
        writed = 0
        tmpbuf = [None] * 4
        ended = False
        while writed < n and not ended:
            length = Reader.read4(tmpbuf)
            if length < 4:
                ended = True
            for i in range(length):
                buf[writed] = tmpbuf[i]
                writed += 1
                if writed == n: break
        return writed