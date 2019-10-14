'''
Title     : 314. Binary Tree Vertical Order Traversal ($$$)
Problem   : https://leetcode.com/problems/binary-tree-vertical-order-traversal/description/
          : https://www.lintcode.com/problem/binary-tree-vertical-order-traversal/description
'''
# Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None

''' Reference: https://www.itread01.com/content/1497880934.html '''
import collections
class Solution:
    def verticalOrder(self, root):
        if not root: return []
        columns = collections.defaultdict(list)
        queue = collections.deque([(root, 0)])
        while queue:
            node, col = queue.popleft()
            columns[col].append(node.val)
            if node.left:
                queue.append((node.left, col-1))
            if node.right:
                queue.append((node.right, col+1))
        return [columns[i] for i in sorted(columns.keys())]