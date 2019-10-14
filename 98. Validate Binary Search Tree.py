'''
Title     : 98. Validate Binary Search Tree
Problem   : https://leetcode.com/problems/validate-binary-search-tree/
'''
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
'''
recursive solution, divide-and-conquer explicitly based on tree structure i.e. (left, node, right)
Reference: https://leetcode.com/problems/validate-binary-search-tree/discuss/32378/Python-iterative-and-recursive-solutions-with-comments
'''
class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        imin, imax = -(1<<31)-1, 1<<31   # imin = -(1<<31)+1 would fail one test
        return self.helper(root, imin, imax)
    
    def helper(self, root, imin, imax):
        if not root:
            return True
        if not root.left and not root.right:
            if imin < root.val < imax: return True
            else: return False
        if not root.left and root.right:
            return root.val < root.right.val and self.helper(root.right, root.val, imax)
        elif root.left and not root.right:
            return root.left.val < root.val and self.helper(root.left, imin, root.val)
        else:
            return root.left.val < root.val < root.right.val and \
                    self.helper(root.left, imin, root.val) and \
                    self.helper(root.right, root.val, imax)
'''
a cleaner recursive implementation using helper function, divide-and-conquer implicitly based on tree structure
Reference: https://leetcode.com/problems/validate-binary-search-tree/discuss/32153/Python-version-based-on-inorder-traversal
'''
class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        vals = []
        self.inOrder(root, vals)
        for i in range(1, len(vals)):
            if vals[i-1] >= vals[i]:
                return False
        return True
    
    def inOrder(self, root, vals):
        if root is None: return []
        self.inOrder(root.left, vals)
        vals.append(root.val)
        self.inOrder(root.right, vals)
'''
iterative solution, directly adapted from the 94. solution, just add the validation step
Reference: https://leetcode.com/problems/validate-binary-search-tree/discuss/32378/Python-iterative-and-recursive-solutions-with-comments
'''
class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        if not root: return True
        stack, vals = [], []
        while True:
            while root:
                stack.append(root)
                root = root.left
            if not stack:
                return True
            node = stack.pop()
            if vals and vals[-1] >= node.val:
                return False
            vals.append(node.val)
            root = node.right
'''
a clearer representation of vals[-1], traverse through the BST
Reference: https://leetcode.com/problems/validate-binary-search-tree/discuss/166691/Python-solution
'''
class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        if not root: return True
        stack, node = [], root
        prev = -float('inf')
        while node or stack:
            if node:
                stack.append(node)
                node = node.left
            else:
                node = stack.pop()
                if node:
                    if node.val <= prev:
                        return False
                    prev = node.val
                node = node.right
        return True