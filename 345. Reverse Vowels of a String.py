'''
Title     : 345. Reverse Vowels of a String
Problem   : https://leetcode.com/problems/reverse-vowels-of-a-string/
'''
'''
use regex and re.findall() and/or re.sub()
Reference: https://leetcode.com/problems/reverse-vowels-of-a-string/discuss/81262/1-2-lines-PythonRuby
'''
import re
class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = re.findall('(?i)[aeiou]', s)
        return re.sub('(?i)[aeiou]', lambda m: vowels.pop(), s)

class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = (c for c in reversed(s) if c in 'aeiouAEIOU')
        # vowels = [c for c in reversed(s) if c in 'aeiouAEIOU'] produces error since list is not a generator class, but tuple is
        return re.sub('(?i)[aeiou]', lambda m: next(vowels), s)

''' direct iterative solution '''
class Solution(object):
    def reverseVowels(self, s):
        vowels = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}
        s = list(s)
        i, j = 0, len(s) - 1
        while i < j:
            while i < len(s) and s[i] not in vowels:
                i += 1
            while 0 <= j and s[j] not in vowels:
                j -= 1
            if i < j:
                s[i], s[j] = s[j], s[i]
                i += 1; j -= 1
        return ''.join(s)