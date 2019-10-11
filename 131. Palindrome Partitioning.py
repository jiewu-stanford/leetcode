'''
Title     : 131. Palindrome Partitioning
Problem   : https://leetcode.com/problems/palindrome-partitioning/description/
'''
'''
recursive solution
Reference: https://leetcode.com/problems/palindrome-partitioning/discuss/42025/1-liner-Python-Ruby
'''
class Solution:
    def partition(self, s: str) -> List[List[str]]:
        if not s: return [[]]
        res = []
        for i in range(1, len(s)+1):
            if s[:i] == s[i-1::-1]:
                for rem in self.partition(s[i:]):
                    res.append([s[:i]] + rem)
        return res