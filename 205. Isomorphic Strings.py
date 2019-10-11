'''
Title     : 205. Isomorphic Strings
Problem   : https://leetcode.com/problems/isomorphic-strings/
'''
'''
use dictionary to record position
Reference: https://leetcode.com/problems/isomorphic-strings/discuss/57941/Python-different-solutions-(dictionary-etc)
'''
class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        d1, d2 = {}, {}
        for i, val in enumerate(s):
            d1[val] = d1.get(val,[]) + [i]
        for i, val in enumerate(t):
            d2[val] = d2.get(val,[]) + [i]
        return sorted(d1.values()) == sorted(d2.values())

''' use find() + list comprehension, ibid. '''
class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        return [s.find(i) for i in s] == [t.find(j) for j in t]

''' the list comprehension can be simplified using map(), ibid. '''
class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        return list(map(s.find, s)) == [t.find(j) for j in t]

''' clever use of zip and set() for distinct elements, ibid. '''
class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        return len(set(zip(s,t))) == len(set(s)) == len(set(t))

''' loop comparison using ASCII number, ibid. '''
class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        d1, d2 = [0 for _ in range(256)], [0 for _ in range(256)]
        for i in range(len(s)):
            if d1[ord(s[i])] != d2[ord(t[i])]:
                return False
            d1[ord(s[i])] = i + 1
            d2[ord(t[i])] = i + 1
        return True