'''
Title     : 393. UTF-8 Validation
Problem   : https://leetcode.com/problems/utf-8-validation/
'''
''' Reference: https://leetcode.com/problems/utf-8-validation/discuss/87494/Short'n'Clean-12-lines-Python-solution '''
class Solution:
    def validUtf8(self, data: List[int]) -> bool:
        def check(data, startindex, size):
            for i in range(startindex+1, startindex+size+1):
                if i >= len(data) or (data[i]>>6) != 0b10:
                    return False
            return True
        
        if not data: return False
        start = 0
        while start < len(data):
            first = data[start]
            if (first >> 3) == 0b11110  and check(data, start, 3):  start += 4
            elif (first >> 4) == 0b1110 and check(data, start, 2):  start += 3
            elif (first >> 5) == 0b110  and check(data, start, 1):  start += 2
            elif (first >> 7) == 0:                                 start += 1
            else: return False
        return True