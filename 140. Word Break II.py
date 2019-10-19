'''
Title     : 140. Word Break II
Problem   : https://leetcode.com/problems/word-break-ii/description/
'''
'''
recursive solution using list comprehension
Reference: https://leetcode.com/problems/word-break-ii/discuss/44169/9-lines-Python-10-lines-C%2B%2B
'''
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        memo = {len(s): ['']}
        def sentences(i):   # returns a list of all sentences that can be built from the suffix s[i:]
            if i not in memo:
                memo[i] = [s[i:j] + (' ' + tail if tail else tail)   # (tail and ' '+tail)
                            for j in range(i+1, len(s)+1) if s[i:j] in wordDict
                            for tail in sentences(j)]
            return memo[i]
        return sentences(0)
'''
list comprehension spelled out, with the key of the memory dictionary changed from length to substring
Reference: https://leetcode.com/problems/word-break-ii/discuss/44311/Python-easy-to-understand-solution
'''
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        return self.helper(s, wordDict, {})

    def helper(self, s, wordDict, memo):
        if not s: return []
        if s in memo: return memo[s]
        res = []
        for word in wordDict:
            if not s.startswith(word): continue
            if len(word) == len(s):
                res.append(word)
            else:
                tails = self.helper(s[len(word):], wordDict, memo)
                for tail in tails:
                    sentence = word + ' ' + tail
                    res.append(sentence)
        memo[s] = res
        return res