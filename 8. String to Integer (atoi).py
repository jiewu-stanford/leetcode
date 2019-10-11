'''
Title     : 8. String to Integer (atoi) (XXX)
Problem   : https://leetcode.com/problems/string-to-integer-atoi/
'''
import re
class Solution:
    def myAtoi(self, str: str) -> int:
        numStr = re.findall('^[\+\-]?0*\d+', str.strip())
        
        minInt = 0 - 2**31
        maxInt = 2**31 - 1
        if numStr:
            num = int(numStr[0])
            if num > maxInt:
                return maxInt
            elif num < minInt:
                return minInt
            else:
                return num
        else:
            return 0