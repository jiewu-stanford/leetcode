'''
Title     : 316. Remove Duplicate Letters
Problem   : https://leetcode.com/problems/remove-duplicate-letters/
'''
'''
recursive solution using counter()
Reference: https://leetcode.com/problems/remove-duplicate-letters/discuss/76768/A-short-O(n)-recursive-greedy-solution
'''
import collections
class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        if not s: return ''
        count = collections.Counter(list(s))
        pos = 0
        for i, c in enumerate(s):
            if c < s[pos]: pos = i   # < enforces lexicographical order
            count[c] -= 1
            if count[c] == 0: break   # stops at the last repeated position
        return s[pos] + self.removeDuplicateLetters(s[pos+1:].replace(s[pos], ''))
'''
a faster way of finding the last repeated position without using counter() and enforcing lexicographic order using sorted()
Reference: https://leetcode.com/problems/remove-duplicate-letters/discuss/76787/Some-Python-solutions
'''
class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        if not s: return ''
        for c in sorted(set(s)):
            suffix = s[s.index(c):]
            if set(suffix) == set(s):   # only suffix containing the last repeated c satisfies ==
                return c + self.removeDuplicateLetters(suffix.replace(c, ''))
        return ''

''' iterative solution using the built-in .rindex() function to find the last repeated position, ibid. '''
class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        res = ''
        while s:
            i = min(map(s.rindex, set(s)))   # only set converted from string has the .rindex() method, general set does not
            c = min(s[:i+1])
            res += c
            s = s[s.index(c):].replace(c, '')
        return res
'''
iterative solution using stack and counter(), instead of finding the last repeated position use visited set and continue to ensure recording only once
Reference: https://leetcode.com/problems/remove-duplicate-letters/discuss/76769/Java-solution-using-Stack-with-comments
'''
import collections
class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        count, visited, stack = collections.Counter(s), set(), []
        for c in s:
            count[c] -= 1
            if c in visited: continue
            while stack and c < stack[-1] and count[stack[-1]] > 0:   # count > 0 to ensure the unique character would not be popped out despite
                                                                      # violating the lexicographical order e.g. 'cbacdcbc' -> 'acdb' although 'd' > 'b'
                visited.remove(stack.pop())
            stack.append(c)
            visited.add(c)
        return ''.join(stack)