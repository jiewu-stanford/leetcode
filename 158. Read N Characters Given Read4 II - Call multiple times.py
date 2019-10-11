'''
Title     : 158. Read N Characters Given Read4 II - Call multiple times ($$$)
Problem   : https://leetcode.com/problems/read-n-characters-given-read4-ii-call-multiple-times/
          : https://www.lintcode.com/problem/read-n-characters-given-read4-ii-call-multiple-times/description
'''
''' Reference: https://github.com/shiyanhui/Algorithm/blob/master/LeetCode/Python/158%20Read%20N%20Characters%20Given%20Read4%20II.py '''
class Reader:
    def read4(self, buf): pass
    
class Solution(object):
    def __init__(self):
        self.rem = []

    def read(self, buf, n):
        count, reads = 0, [''] * 4
        if self.rem:
            while count < min(n, len(self.rem)):
                buf[count] = self.rem[count]
                count += 1
            self.rem = self.rem[count:]
        while count < n:
            size = Reader.read4(reads)
            if not size: break
            length = min(n - count, size)
            self.rem = reads[length : size]
            for i in range(length):
                buf[count] = reads[i]
                count += 1
        return count

''' Reference: https://www.cnblogs.com/lightwindy/p/8481800.html '''
class Solution(object):
    def __init__(self):
        self.__buf4 = [''] * 4
        self.__i4 = 0
        self.__n4 = 0

    def read(self, buf, n):
        i = 0
        while i < n:
            if self.__i4 < self.__n4:   # check whether there is any character in buf4
                buf[i] = self.__buf4[self.__i4]
                i += 1
                self.__i4 += 1
            else:
                self.__n4 = Reader.read4(self.__buf4)
                if self.__n4:
                    self.__i4 = 0
                else:
                    break
        return i