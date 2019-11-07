'''
Title     : 443. String Compression
Problem   : https://leetcode.com/problems/string-compression/
'''
'''
two-pointer strategy, one read pointer (i) + one write pointer (j)
Reference: https://leetcode.com/problems/string-compression/discuss/92568/Python-Two-Pointers-O(n)-time-O(1)-space
'''
class Solution:
    def compress(self, chars: List[str]) -> int:
        i = j = 0
        while i < len(chars):
            c, freq = chars[i], 0
            while i < len(chars) and chars[i] == c:
                i, freq = i+1, freq+1
            chars[j], j = c, j+1
            if freq > 1:
                for digit in str(freq):
                    chars[j], j = digit, j+1
        return j