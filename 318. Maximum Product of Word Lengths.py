'''
Title     : 318. Maximum Product of Word Lengths
Problem   : https://leetcode.com/problems/maximum-product-of-word-lengths/
'''
'''
without using bit manipulation
Reference: https://leetcode.com/problems/maximum-product-of-word-lengths/discuss/76989/Python-accepted-solution
'''
class Solution:
    def maxProduct(self, words: List[str]) -> int:
        if not words: return 0
        res = 0
        while words:
            curr_word = set(words[0])
            curr_len = len(words[0])
            words = words[1:]
            for word in words:
                for c in curr_word:
                    if c in word:
                        break
                else:
                    res = max(res, curr_len*len(word))
        return res
'''
bit manipulation, converting words to ASCII numbers, TLE if using set intersection if not set(words[i]).intersection(set(words[j])):
Reference: http://bookshadow.com/weblog/2015/12/16/leetcode-maximum-product-word-lengths/
'''
class Solution:
    def maxProduct(self, words: List[str]) -> int:
        if not words: return 0
        nums = []
        for word in words:
            nums += sum(1 << (ord(c)-ord('a')) for c in set(word)),   # sum(2 raised to the power of ord(x)-ord('a')), and convert int to tuple by ,
            
        res = 0
        n = len(words)
        for i in range(n):
            for j in range(n):
                if not (nums[i] & nums[j]):
                    res = max(res, len(words[i])*len(words[j]))
        return res
'''
bit manipulation, use dictionary to keep length, without sort the word-to-num conversion will miss several tuples which I also don't know why
Reference: https://leetcode.com/problems/maximum-product-of-word-lengths/discuss/77029/A-two-line-Python-solution-176-ms
'''
class Solution:
    def maxProduct(self, words: List[str]) -> int:
        if not words: return 0
        d = {sum(1 << (ord(c)-ord('a')) for c in set(w)): len(w) for w in sorted(words, key=len)}.items()   # .items() is to make it iterable
        return max([l1*l2 for n1, l1 in d for n2, l2 in d if not n1 & n2] or [0])