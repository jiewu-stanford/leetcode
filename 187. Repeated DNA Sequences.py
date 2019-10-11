'''
Title     : 187. Repeated DNA Sequences
Problem   : https://leetcode.com/problems/repeated-dna-sequences/description/
'''
class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        repeated, recorded = set(), set()
        for i in range(len(s)-9):
            substr = s[i:i+10]
            if substr in recorded:
                repeated.add(substr)
            else:
                recorded.add(substr)
        return list(repeated)

class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        d = dict()
        for substr in [s[i:i+10] for i in range(len(s)-9)]:
            d[substr] = d.get(substr, 0) + 1
        return [key for key, val in d.items() if val > 1]