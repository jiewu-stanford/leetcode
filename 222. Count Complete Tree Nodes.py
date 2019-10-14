'''
Title     : 222. Count Complete Tree Nodes
Problem   : https://leetcode.com/problems/count-complete-tree-nodes/description/
'''
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
'''
iterative solution
Reference: https://leetcode.com/problems/count-complete-tree-nodes/discuss/62002/Clean-python-code
'''
class Solution:
    def countNodes(self, root: TreeNode) -> int:
        if not root: return 0
        h = self.height(root)
        res = 0
        while root:
            lh, rh = self.height(root.left), self.height(root.right)
            if lh <= rh:
                res += 2**lh   # number of nodes in left half = 2**lh - 1 and +1 which is root
                root = root.right
            else:
                res += 2**rh
                root = root.left
            h -= 1
        return res
    
    def height(self, root):
        height = 0
        while root:
            height += 1
            root = root.left
        return height
'''
recursive solution
Reference: https://leetcode.com/problems/count-complete-tree-nodes/discuss/62073/Python-O(lgn)*O(lgn)-solution-with-comments
'''
class Solution:
    def countNodes(self, root: TreeNode) -> int:
        if not root: return 0
        lh, rh = self.height(root.left), self.height(root.right)
        if lh <= rh:
            return 2**lh + self.countNodes(root.right)
        else:
            return self.countNodes(root.left) + 2**rh
    
    def height(self, root):
        return 0 if not root else 1 + self.height(root.left)