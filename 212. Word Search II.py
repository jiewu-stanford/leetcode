'''
Title     : 212. Word Search II
Problem   : https://leetcode.com/problems/word-search-ii/
'''
'''
direct implementation of trie, using recursive helper function
Reference: https://leetcode.com/problems/word-search-ii/discuss/59790/Python-dfs-solution-(directly-use-Trie-implemented)
'''
import collections
class Node:
    def __init__(self):
        self.word = ''
        self.children = collections.defaultdict(Node)

class Trie:
    def __init__(self):
        self.root = Node()

    def add(self, word):
        node = self.root
        for c in word:
            node = node.children[c]
        node.word = word

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        if not board: return []
        t = Trie()
        for word in words:
            t.add(word)
        res, self.rows, self.cols = [], len(board), len(board[0])
        for i, line in enumerate(board):
            for j, c in enumerate(line):
                if c in t.root.children:
                    res = self.helper(board, t.root.children[c], i, j, res)
        return res
    
    def helper(self, board, node, x, y, res):
        if node.word:
            res.append(node.word)
            node.word = ''
        directions = [(0,-1), (0,1), (-1,0), (1,0)]
        curr, board[x][y] = board[x][y], '-'   # assigned '-' means deleted, since each char can only be used once in a word
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < self.rows and 0 <= ny < self.cols and board[nx][ny] in node.children:
                res = self.helper(board, node.children[board[nx][ny]], nx, ny, res)
        board[x][y] = curr   # char can be reused for different words thus restored e.g. 't' in 'oath' and 'eat' in the example
        return res