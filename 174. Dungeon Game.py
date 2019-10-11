'''
Title     : 174. Dungeon Game
Problem   : https://leetcode.com/problems/dungeon-game/
'''
'''
2D DP solution, but note that DP is running 'backword' i.e. from right to left, from bottom to top
Reference: https://leetcode.com/problems/dungeon-game/discuss/52869/Python-easy-to-understand-solutions-(O(m*n)-O(n)-space)
'''
class Solution:
    def calculateMinimumHP(self, dungeon: List[List[int]]) -> int:
        if not dungeon: return
        r, c = len(dungeon), len(dungeon[0])
        
        dp = [[0]*c for _ in range(r)]
        dp[-1][-1] = max(1, 1-dungeon[-1][-1])
        for j in range(c-2, -1, -1):
            dp[-1][j] = max(1, dp[-1][j+1]-dungeon[-1][j])
        for i in range(r-2, -1, -1):
            dp[i][-1] = max(1, dp[i+1][-1]-dungeon[i][-1])
            
        for i in range(r-2, -1, -1):
            for j in range(c-2, -1, -1):
                dp[i][j] = max(1, min(dp[i+1][j], dp[i][j+1])-dungeon[i][j])
        return dp[0][0]

''' condensed into 1D DP through in-place update for each row, ibid. '''
class Solution:
    def calculateMinimumHP(self, dungeon: List[List[int]]) -> int:
        if not dungeon: return
        r, c = len(dungeon), len(dungeon[0])
        
        dp = [0]*c
        dp[-1] = max(1, 1-dungeon[-1][-1])
        for j in range(c-2, -1, -1):
            dp[j] = max(1, dp[j+1]-dungeon[-1][j])
            
        for i in range(r-2, -1, -1):
            dp[-1] = max(1, dp[-1]-dungeon[i][-1])
            for j in range(c-2, -1, -1):
                dp[j] = max(1, min(dp[j], dp[j+1])-dungeon[i][j])
        return dp[0]