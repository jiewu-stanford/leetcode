'''
Title     : 336. Palindrome Pairs
Problem   : https://leetcode.com/problems/palindrome-pairs/
'''
'''
isolate the non-palindrome part (prefix/suffix) to match for getting a palindrome
Reference: https://leetcode.com/problems/palindrome-pairs/discuss/79209/Accepted-Python-Solution-With-Explanation
'''
class Solution:
    def palindromePairs(self, words: List[str]) -> List[List[int]]:
        if not words: return [[]]
        d = {w: i for i, w in enumerate(words)}
        res = []
        for i, w in enumerate(words):
            for j in range(len(w)+1):
                pre, suf = w[:j], w[j:]
                if pre==pre[::-1] and suf[::-1]!=w and suf[::-1] in d:
                    res.append([d[suf[::-1]], i])   # palindrome prefix e.g. 'lls' and 's', 'sssll' and 'lls' in Example 1
                if suf==suf[::-1] and pre[::-1]!=w and pre[::-1] in d and j != len(w):
                    res.append([i, d[pre[::-1]]])   # palindrome suffix e.g. 'sll' and 's'
        return res
'''
brute force using trie structure (use dict to mimick a trie node)
Reference: https://leetcode.com/problems/palindrome-pairs/discuss/79240/Python-Solution-with-Trie
'''
from functools import reduce
class Solution:
    def ispalin(self, s):
        return s == s[::-1]

    def palindromePairs(self, words: List[str]) -> List[List[int]]:
        res, root = [], {}
        for i, word in enumerate(words):
            curr = root
            for j, c in enumerate(word):
                if c not in curr: curr[c] = {}
                curr = curr[c]
                rem = word[j+1:]
                if rem and self.ispalin(rem):
                    curr.setdefault('indx', []).append(i)   # keep the index of the word in 'indx' if it contains palindrome suffix
            curr['isword'] = i                              # keep the index of the word in 'isword' if it contains no palindrome suffix

        for i, word in enumerate(words):
            revword = word[::-1]
            curr = root
            fail = False
            for j, c in enumerate(revword):
                if c not in curr: fail = True; break
                else: curr = curr[c]
                k = curr.get('isword')
                if k is not None and k != i and self.ispalin(revword[j+1:]):
                    res.append([k, i])
            if not fail and 'indx' in curr:
                res.extend([k, i] for k in curr["indx"] if k != i)
        
        if '' in words:
            j = words.index('')
            res.extend(reduce(lambda x,y:x+y, ([[i,j],[j,i]] for i, w in enumerate(words) if w and self.ispalin(w))))
        return res