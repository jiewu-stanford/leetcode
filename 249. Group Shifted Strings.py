'''
Title     : 249. Group Shifted Strings ($$$)
Problem   : https://leetcode.com/problems/group-shifted-strings/
          : https://www.lintcode.com/problem/group-shifted-strings/description
'''
'''
very simlar to anagrams but use ASCII number shift instead
Reference: http://www.voidcn.com/article/p-mjnjyrnt-zo.html
'''
import collections
class Solution:
    def groupStrings(self, strings):
        groups = collections.defaultdict(list)
        for s in strings:
            key = tuple([(ord(c) - ord(s[0])) % 26 for c in s])   # tuple(sorted(s))
            groups[key].append(s)
        return [sorted(val) for val in groups.values()]