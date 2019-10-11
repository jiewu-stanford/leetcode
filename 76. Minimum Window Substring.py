'''
Title     : 76. Minimum Window Substring
Problem   : https://leetcode.com/problems/minimum-window-substring/
'''
'''
use deque() type for sliding window problems, because it offers the convenience of popleft()
however this problem is NOT a sliding window problem because the window length is increasing
Reference : https://leetcode.com/problems/minimum-window-substring/discuss/26826/Python-Simple-Solution
'''
import collections
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        length = 0
        dictT = collections.Counter(t)
        dictS = {}
        l, r = 0, float('inf')
        
        slider = collections.deque([])
        for i, c in enumerate(s):
            if c in dictT:
                slider.append(i)
                dictS[c] = dictS.get(c, 0) + 1
                if dictS[c] <= dictT[c]:
                    length += 1
                while slider and dictS[s[slider[0]]] > dictT[s[slider[0]]]:   # if there is another substring that contains t
                    dictS[s[slider.popleft()]] -= 1
                if length == len(t) and slider[-1]-slider[0] < r-l:
                    l, r = slider[0], slider[-1]
        return s[l:r+1] if r != float('inf') else ''
'''
use Counter() instead of two dictionaries
Reference: https://leetcode.com/problems/minimum-window-substring/discuss/26804/12-lines-Python
'''
import collections
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        length = len(t)
        count = collections.Counter(t)
        
        l, r, i = 0, float('inf'), 0
        for j, c in enumerate(s, 1):
            if count[c] > 0: length -= 1
            count[c] -= 1
            if length == 0:
                while i < j and count[s[i]] < 0:
                    count[s[i]] += 1
                    i += 1   # shrink window
                if r == float('inf') or j - i < r - l:
                    l, r = i, j
                
        return s[l:r] if r != float('inf') else ''

''' use defaultdict() instead of Counter() '''
import collections
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        length = len(t)
        dictT = collections.defaultdict(int)
        for c in t: dictT[c] += 1

        l, r, i = 0, float('inf'), 0
        for j, c in enumerate(s, 1):
            if dictT[c] > 0: length -= 1
            dictT[c] -= 1
            if length == 0:
                while dictT[s[i]] < 0:
                    dictT[s[i]] += 1
                    i += 1   # shrink window
                if r == float('inf') or j - i < r - l:
                    l, r = i, j
                
        return s[l:r] if r != float('inf') else ''