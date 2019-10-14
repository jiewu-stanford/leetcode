'''
Title     : 112. Path Sum
Problem   : https://leetcode.com/problems/path-sum/
'''
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
'''
simple DFS (bottom-up) recursive solution
Reference: https://leetcode.com/problems/path-sum/discuss/36360/Short-Python-recursive-solution-O(n)
'''
class Solution:
    def hasPathSum(self, root: TreeNode, sum: int) -> bool:
        if not root: return False
        if not root.left and not root.right and root.val == sum: return True
        return self.hasPathSum(root.left, sum-root.val) or self.hasPathSum(root.right, sum-root.val)
'''
DFS stack solution
Reference: https://leetcode.com/problems/path-sum/discuss/36486/Python-solutions-(DFS-recursively-DFS%2Bstack-BFS%2Bqueue)
'''
class Solution:
    def hasPathSum(self, root: TreeNode, sum: int) -> bool:
        if not root: return False
        stack = [(root, sum)]
        while stack:
            node, value = stack.pop()
            if node:
                if not node.left and not node.right and node.val == value:
                    return True
                if node.right:
                    stack.append((node.right, value-node.val))
                if node.left:
                    stack.append((node.left, value-node.val))
        return False

''' BFS queue solution, ibid. '''
class Solution:
    def hasPathSum(self, root: TreeNode, sum: int) -> bool:
        if not root: return False
        queue = deque([(root, sum)])
        while queue:
            node, value = queue.popleft()
            if node:
                if not node.left and not node.right and node.val == value:
                    return True
                if node.left:
                    queue.append((node.left, value-node.val))
                if node.right:
                    queue.append((node.right, value-node.val))
        return False