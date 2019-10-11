'''
Title     : 79. Word Search
Problem   : https://leetcode.com/problems/word-search/description/
'''
'''
recursive DFS helper function
Reference: https://leetcode.com/problems/word-search/discuss/27660/Python-dfs-solution-with-comments
'''
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        if not board: return False
        for i in range(len(board)):
            for j in range(len(board[0])):
                if self.helper(board, i, j, word):
                    return True
        return False
    
    def helper(self, board, i, j, word):
        if not word: return True
        if i<0 or i>=len(board) or j<0 or j>=len(board[0]) or word[0]!=board[i][j]:
            return False
        tmp, board[i][j] = board[i][j], '$'   # marked as visited to avoid going back and used twice
        res = self.helper(board, i+1, j, word[1:]) or self.helper(board, i-1, j, word[1:]) or \
              self.helper(board, i, j+1, word[1:]) or self.helper(board, i, j-1, word[1:])
        board[i][j] = tmp
        return res
'''
instead of searching for characters on neighboring positions, find the positions and check whether they are adjacent
Reference: https://leetcode.com/problems/word-search/discuss/27751/Clean-Python-Solution
'''
from collections import defaultdict
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        if not board: return False
        char2pos = defaultdict(list)
        for i in range(len(board)):
            for j in range(len(board[0])):
                char2pos[board[i][j]].append((i, j))
        return self.isFound(char2pos, word, set())
    
    def isFound(self, char2pos, word, used, lastPos=None):
        if not word: return True
        for c in char2pos[word[0]]:
            if c in used or (lastPos and not self.isValid(c,lastPos)): continue   # lastPos and not self.isValid(c,lastPos) is used for repeated characters
            used.add(c)
            if self.isFound(char2pos, word[1:], used, c): return True
            used.remove(c)   # get ready for checking the next occurrence
        return False
    
    def isValid(self, pos1, pos2):
        return (pos1[0]==pos2[0] and abs(pos1[1]-pos2[1])==1) or (pos1[1]==pos2[1] and abs(pos1[0]-pos2[0])==1)