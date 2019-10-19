'''
Title     : 208. Implement Trie (Prefix Tree)
Problem   : https://leetcode.com/problems/implement-trie-prefix-tree/description/
'''
''' Reference: https://leetcode.com/problems/implement-trie-prefix-tree/discuss/58834/AC-Python-Solution '''
import collections
class TrieNode:
    def __init__(self):
        self.children = collections.defaultdict(TrieNode)
        self.isWord = False

class Trie(object):
    
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        curr = self.root
        for c in word:
            curr = curr.children[c]
        curr.isWord = True

    def search(self, word):
        curr = self.root
        for c in word:
            curr = curr.children.get(c)
            if not curr: return False
        return curr.isWord

    def startsWith(self, prefix):
        curr = self.root
        for c in prefix:
            curr = curr.children.get(c)
            if not curr: return False
        return True
        
# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)