'''
Title     : 139. Word Break
Problem   : https://leetcode.com/problems/word-break/
'''
'''
standard 1D DP solution
Reference: https://leetcode.com/problems/word-break/discuss/44035/Python-concise-dp-solution
'''
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp = [False] * (len(s) + 1)
        dp[0] = True
        for i in range(1, len(s)+1):
            for j in range(i):
                if dp[j] and s[j:i] in wordDict:
                    dp[i] = True
                    break
        return dp[-1]
'''
BFS iterative solution using queue and with cache, increment based on lengths of words
Reference: https://leetcode.com/problems/word-break/discuss/43951/Python-BFS-beats-95
'''
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        queue = [0]
        lenList = [l for l in set(map(len, wordDict))]
        visited = set()   # cache for used starting positions in s
        while queue:
            startindex = queue.pop(0)
            if startindex in visited:
                continue
            visited.add(startindex)
            for l in lenList:
                if s[startindex:startindex+l] in wordDict:
                    if startindex + l == len(s):
                        return True
                    queue.append(startindex + l)
        return False
'''
DFS iterative solution using stack and with cache, and with the convenience provided by .startswith() function
Reference: https://leetcode.com/problems/word-break/discuss/130922/python-DFS-98
'''
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        stack = [0]
        visited = set()   # cache for used starting positions in s
        while stack:
            startindex = stack.pop(0)
            if startindex in visited:
                continue
            visited.add(startindex)
            for word in wordDict:
                if s[startindex:].startswith(word):
                    l = len(word)
                    if startindex + l == len(s):
                        return True
                    stack.append(startindex + l)
        return False