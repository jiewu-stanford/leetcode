'''
Title     : 230. Kth Smallest Element in a BST
Problem   : https://leetcode.com/problems/kth-smallest-element-in-a-bst/
'''
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
'''
iterative solution use deque
Reference: https://leetcode.com/problems/kth-smallest-element-in-a-bst/discuss/63734/O(k)-space-O(n)-time-10%2B-short-lines-3-solutions
'''
import collections
class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        queue = collections.deque()
        while root or queue:
            while root:
                queue.append(root)
                root = root.left
            root = queue.pop()
            if k == 1: return root.val
            k -= 1
            root = root.right
'''
iterative solution using stack instead
Reference: https://leetcode.com/problems/kth-smallest-element-in-a-bst/discuss/63829/Python-Easy-Iterative-and-Recursive-Solution
'''
class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        stack = []
        while root or stack:
            while root:
                stack.append(root)
                root = root.left
            root = stack.pop()
            if k == 1: return root.val
            k -= 1
            root = root.right
'''
DFS recursive helper function to exhause the entire tree
Reference: https://leetcode.com/problems/kth-smallest-element-in-a-bst/discuss/63660/3-ways-implemented-in-JAVA-(Python)%3A-Binary-Search-in-order-iterative-and-recursive
'''
class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        count = []
        self.helper(root, count)
        return count[k-1]

    def helper(self, node, count):
        if not node: return
        self.helper(node.left, count)
        count.append(node.val)
        self.helper(node.right, count)