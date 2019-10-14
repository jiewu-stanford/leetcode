'''
Title     : 173. Binary Search Tree Iterator
Problem   : https://leetcode.com/problems/binary-search-tree-iterator/
'''
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

''' Reference: https://leetcode.com/problems/binary-search-tree-iterator/discuss/52525/My-solutions-in-3-languages-with-Stack '''
class BSTIterator:

    def __init__(self, root: TreeNode):
        self.stack = list()
        self.pushAll(root)   # push in all leftmost nodes of root

    def next(self) -> int:
        node = self.stack.pop()
        self.pushAll(node.right)   # push in the right branch of current node
        return node.val

    def hasNext(self) -> bool:
        return self.stack

    def pushAll(self, root: TreeNode):
        while root:
            self.stack.append(root)
            root = root.left

# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()