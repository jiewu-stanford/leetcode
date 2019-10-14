'''
Title     : 99. Recover Binary Search Tree
Problem   : https://leetcode.com/problems/recover-binary-search-tree/
'''
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
'''
recursive helper function two-pass collecting all node values and then searching for reversed orders
Reference: https://leetcode.com/problems/recover-binary-search-tree/discuss/32624/Python-iterative-solution-(average-O(lgn)-space-one-pass).
'''
class Solution:
    def recoverTree(self, root: TreeNode) -> None:
        if not root: return
        res = self.helper(root, [])
        first, second = None, None
        for i in range(1, len(res)):
            if not first and res[i-1].val > res[i].val:   # first time order is found reversed
                first, second = res[i-1], res[i]
            if first and res[i-1].val > res[i].val:   # second time order is found reversed
                second = res[i]
        first.val, second.val = second.val, first.val

    def helper(self, root, res):
        if root:
            res = self.helper(root.left, res)
            res.append(root)
            res = self.helper(root.right, res)
        return res
'''
recursive helper function one-pass searching for reversed orders (violated twice, e.g. 1, 2, 3, 4, 5, 6 -> 1, 5, 3, 4, 2, 6 where 5 > 3 and 4 > 2
Reference: https://leetcode.com/problems/recover-binary-search-tree/discuss/32539/Tree-Deserializer-and-Visualizer-for-Python
'''
class Solution:
    def recoverTree(self, root: TreeNode) -> None:
        if not root: return
        def helper(node):
            if node:
                helper(node.left)
                if node.val < self.prev.val:
                    if not self.first:
                        self.first, self.second = self.prev, node
                    else:
                        self.second = node
                self.prev = node
                helper(node.right)
                
        self.first, self.second = None, None
        self.prev = TreeNode(-float('inf'))
        helper(root)
        self.first.val, self.second.val = self.second.val, self.first.val

''' one-pass iterative solution using stack, adapted from the 272. solution '''
class Solution:
    def recoverTree(self, root: TreeNode) -> None:
        if not root: return
        stack, node = [], root
        prev, first, second = None, None, None
        while stack or node:
            if node:
                stack.append(node)
                node = node.left
            else:
                node = stack.pop()
                if prev and node.val < prev.val:
                    if not first:
                        first, second = prev, node
                    else:
                        second = node
                prev = node
                node = node.right
        first.val, second.val = second.val, first.val
'''
true O(1) space solution using Morris traversal
Reference: https://leetcode.com/problems/recover-binary-search-tree/discuss/32582/SIMPLE-Python-solution-with-REAL-O(1)-space-by-using-Morris-traversal-(with-comments)
'''
class Solution:
    def recoverTree(self, root: TreeNode) -> None:
        if not root: return
        curr, prev, first, second, predecessor = root, None, None, None, None
        while curr:
            if not curr.left:
                if predecessor and curr.val < predecessor.val:   # link with predecessor is already established, and reversed order is found
                    if not first: first = predecessor
                    second = curr
                predecessor = curr
                curr = curr.right
            else:   # checking the right, find predecessor and make curr its right child
                prev = curr.left
                while prev.right and prev.right != curr:
                    prev = prev.right
                if not prev.right:
                    prev.right = curr    # establish link
                    curr = curr.left
                else:   # curr's turn, visited and link already established thus no need to push left via curr = curr.left
                    if predecessor and curr.val < predecessor.val:
                        if not first: first = predecessor
                        second = curr
                    predecessor = curr
                    prev.right = None   # delete the link after visited
                    curr = curr.right
        first.val, second.val = second.val, first.val