'''
Title     : 97. Interleaving String
Problem   : https://leetcode.com/problems/interleaving-string/
'''
'''
2D DP with O(m*n) space, need 2D since s2 can be interleaved anywhere in s1
Reference: https://leetcode.com/problems/interleaving-string/discuss/31885/Python-DP-solutions-(O(m*n)-O(n)-space)-BFS-DFS
'''
class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        l1, l2, l3 = len(s1), len(s2), len(s3)
        if l1 + l2 != l3: return False
        dp = [[True for _ in range(l2+1)] for _ in range(l1+1)]
        for i in range(1, l1+1):
            dp[i][0] = dp[i-1][0] and s1[i-1] == s3[i-1]
        for j in range(1, l2+1):
            dp[0][j] = dp[0][j-1] and s2[j-1] == s3[j-1]
        for i in range(1, l1+1):
            for j in range(1, l2+1):
                dp[i][j] = (dp[i-1][j] and s1[i-1] == s3[i+j-1]) or \
                            (dp[i][j-1] and s2[j-1] == s3[i+j-1])
        return dp[-1][-1]

''' 1D DP solution, O(n) space, ibid. '''
class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        l1, l2, l3 = len(s1), len(s2), len(s3)
        if l1 + l2 != l3: return False
        dp = [True for _ in range(l2+1)]
        for j in range(1, l2+1):
            dp[j] = dp[j-1] and s2[j-1] == s3[j-1]
        for i in range(1, l1+1):
            dp[0] = dp[0] and s1[i-1] == s3[i-1]
            for j in range(1, l2+1):
                dp[j] = (dp[j] and s1[i-1] == s3[i+j-1]) or \
                            (dp[j-1] and s2[j-1] == s3[i+j-1])
        return dp[-1]

''' DFS using stack, ibid. '''
class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        l1, l2, l3 = len(s1), len(s2), len(s3)
        if l1 + l2 != l3: return False
        stack, visited = [(0, 0)], set((0, 0))
        while stack:
            i, j = stack.pop()   # (i, j) means s1[:i] and s2[:j] have been interleaved
            if i + j == l3:
                return True
            if i+1 <= l1 and s1[i] == s3[i+j] and (i+1,j) not in visited:
                stack.append((i+1, j))
                visited.add((i+1, j))
            if j+1 <= l2 and s2[j] == s3[i+j] and (i,j+1) not in visited:
                stack.append((i, j+1))
                visited.add((i, j+1))
        return False

''' BFS using queue, ibid. '''
from collections import deque
class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        l1, l2, l3 = len(s1), len(s2), len(s3)
        if l1 + l2 != l3: return False
        queue, visited = deque([(0, 0)]), set((0, 0))
        while queue:
            i, j = queue.popleft()
            if i + j == l3:
                return True
            if i+1 <= l1 and s1[i] == s3[i+j] and (i+1,j) not in visited:
                queue.append((i+1, j))
                visited.add((i+1, j))
            if j+1 <= l2 and s2[j] == s3[i+j] and (i,j+1) not in visited:
                queue.append((i, j+1))
                visited.add((i, j+1))
        return False