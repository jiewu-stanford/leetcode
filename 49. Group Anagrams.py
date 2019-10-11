'''
Title     : 49. Group Anagrams
Problem   : https://leetcode.com/problems/group-anagrams/
'''
'''
use default dictionary + sorted string as common key
Reference: https://leetcode.com/problems/group-anagrams/discuss/19216/1-line-RubyPython-for-Updated-Problem
'''
import collections
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = collections.defaultdict(list)
        for s in strs:
            groups[tuple(sorted(s))].append(s)   # tuple to make it immutable thus iterable
        return groups.values()

'''
use ordinary dictionary, need if...else statement to append
Reference: https://leetcode.com/problems/group-anagrams/discuss/19338/Sorting-Python-solution-beats-100
'''
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = {}
        for s in strs:
            w = ''.join(sorted(s))   # string to make it immutable thus iterable
            if w in d: d[w].append(s)
            else: d[w] = [s]
        return d.values()