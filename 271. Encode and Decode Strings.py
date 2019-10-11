'''
Title     : 271. Encode and Decode Strings ($$$) (XXX)
Problem   : https://leetcode.com/problems/remove-duplicate-letters/
          : https://www.lintcode.com/problem/encode-and-decode-strings/description
'''
''' Reference: https://baihuqian.github.io/2018-07-28-encode-and-decode-strings/ '''
class Solution:
    def encode(self, strs):
        if len(strs) == 0: return ''
        else: return '//'.join([s.replace('/','#/!') for s in strs]) + '//'

    def decode(self, str):
        if len(str) == 0: return []
        return [s.replace('#/!', '/') for s in str.split('//')][:-1]