'''
Title     : 72. Edit Distance
Problem   : https://leetcode.com/problems/edit-distance/
'''
''' 
Reference: https://leetcode.com/problems/edit-distance/discuss/274951/Python-Classic-DP (explanation)
Reference: https://github.com/Garvit244/Leetcode/blob/master/1-100q/72.py (code, due to clearer dp generation code)
'''
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        l1, l2 = len(word1), len(word2)
        dp = [[0 for _ in range(l2+1)] for _ in range(l1+1)]   # dp[i][j] = distance between word1[:i] and word2[:j]
        for i in range(l1+1):
            for j in range(l2+1):
                if i == 0:
                    dp[i][j] = j
                elif j == 0:
                    dp[i][j] = i
                elif word1[i-1] == word2[j-1]:
                    dp[i][j] = dp[i-1][j-1]
                else:
                    dp[i][j] = 1 + min(dp[i-1][j], dp[i-1][j-1], dp[i][j-1])
                    # 1 represents insert operation word1[:i-1] --> word1[:i] thus relates dp[i][j] to dp[i-1][j]
                    #              replace operation word1[i] --> word2[j] thus relates dp[i][j] to dp[i-1][j-1]
                    #              insert operation word2[:j-1] --> word2[:j] thus relates dp[i][j] to dp[i][j-1]
        return dp[l1][l2]