'''
Title     : 68. Text Justification
Problem   : https://leetcode.com/problems/text-justification/
'''
'''
Reference : https://leetcode.com/problems/text-justification/discuss/24891/Concise-python-solution-10-lines
'''
class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        res, curr, nchar = [], [], 0
        for w in words:
            if nchar + len(w) + len(curr) > maxWidth:
                for i in range(maxWidth - nchar):
                    curr[i % (len(curr)-1 or 1)] += ' '   # '1' is for the edge case len(curr) == 1
                res.append(''.join(curr))
                curr, nchar = [], 0
            curr += [w]
            nchar += len(w)
        return res + [' '.join(curr).ljust(maxWidth)]