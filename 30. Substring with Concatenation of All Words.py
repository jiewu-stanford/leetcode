'''
Title     : 30. Substring with Concatenation of All Words
Problem   : https://leetcode.com/problems/substring-with-concatenation-of-all-words/
'''
''' the idea is to use range(start, end, word_len) to make word search like character search '''
import collections
class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        if not s or not words or len(s) < len(words)*len(words[0]): return []
        res, k = [], len(words[0])
        
        for l in range(k):
            d = collections.Counter(words)
            for r in range(l+k, len(s)+1, k):
                word = s[r-k:r]
                d[word] -= 1
                while d[word] < 0:
                    d[s[l:l+k]] += 1
                    l += k
                if l + k*len(words) == r:
                    res.append(l)
                    
        return res
'''
a more comprehensible version, comparing a dictionary with the counter instead of creating the counter for each loop iteration, much faster
Reference: https://leetcode.com/problems/substring-with-concatenation-of-all-words/discuss/13669/99ms-Python-O(kmn)-Solution
'''
import collections
class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        if not s or not words or len(s) < len(words)*len(words[0]): return []
        res, k = [], len(words[0])
        count = collections.Counter(words)
        
        for l in range(k):
            d = {}
            for r in range(l, len(s), k):
                word = s[r:r+k]
                if word not in count:
                    l = r + k
                    d = {}
                    continue
                d[word] = d.get(word, 0) + 1
                while d[word] > count[word]:
                    start_w = s[l:l+k]
                    l += k
                    d[start_w] -= 1   # start_w == word? not necessary! but this is sufficient to continue scan
                if d == count:
                    res.append(l)                    
        return res