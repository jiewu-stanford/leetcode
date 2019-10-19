'''
Title     : 388. Longest Absolute File Path
Problem   : https://leetcode.com/problems/longest-absolute-file-path/
'''
''' Reference: https://leetcode.com/problems/longest-absolute-file-path/discuss/86640/python-solution-easy-to-understand '''
class Solution:
    def lengthLongestPath(self, input: str) -> int:
        d, longest = {}, 0
        for line in input.split('\n'):
            if '.' not in line:   # it is a folder
                level = line.count('\t')
                val = len(line.replace('\t',''))
                d[level] = val
            else:   # it is a file
                level = line.count('\t')
                length = sum([d[l] for l in d.keys() if l<level]) + len(line.replace('\t','')) + level   # folder length + file length + spaces for \
                longest = max(longest, length)
        return longest

''' Reference: https://leetcode.com/problems/longest-absolute-file-path/discuss/86619/Simple-Python-solution '''
class Solution:
    def lengthLongestPath(self, input: str) -> int:
        d, longest = {-1: 0}, 0
        for line in input.split('\n'):
            level = line.count('\t')
            d[level] = d[level-1] + len(line) - level
            if line.count('.'):
                longest = max(longest, d[level] + level)   # if it is a file then add back spaces for \ to compare
        return longest