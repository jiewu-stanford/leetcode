'''
Title     : 211. Add and Search Word - Data structure design
Problem   : https://leetcode.com/problems/add-and-search-word-data-structure-design/
'''
'''
DFS recursive helper function
Reference: https://leetcode.com/problems/add-and-search-word-data-structure-design/discuss/59725/Python-easy-to-follow-solution-using-Trie.
'''
import collections
class TrieNode():
    def __init__(self):
        self.children = collections.defaultdict(TrieNode)
        self.isWord = False

class WordDictionary:
    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word):
        curr = self.root
        for c in word:
            curr = curr.children[c]
        curr.isWord = True

    def search(self, word):
        curr = self.root
        self.res = False
        self.helper(curr, word)
        return self.res
    
    def helper(self, node, word):
        if not word:
            if node.isWord:
                self.res = True
        elif word[0] == '.':
            for n in node.children.values():
                self.helper(n, word[1:])
        else:
            node = node.children.get(word[0])
            if not node:
                return
            self.helper(node, word[1:])

''' use normal dictionary instead of defaultdict, use stack to spell out the recursive steps of the dfs helper function, ibid '''
import collections
class TrieNode():
    def __init__(self):
        self.children = {}
        self.isWord = False

class WordDictionary:
    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        curr = self.root
        for c in word:
            if c in curr.children:
                curr = curr.children[c]
            else:
                curr.children[c] = TrieNode()
                curr = curr.children[c]
        curr.isWord = True

    def search(self, word: str) -> bool:
        stack = [(self.root, word)]
        while stack:
            node, w = stack.pop()
            if not w:
                if node.isWord:
                    return True
            elif w[0] == '.':
                for n in node.children.values():
                    stack.append((n, w[1:]))   # self.helper(n, w[1:])
            else:
                if w[0] in node.children:
                    n = node.children.get(w[0])
                    stack.append((n, w[1:]))

# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)