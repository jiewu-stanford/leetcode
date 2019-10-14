'''
Title     : 272. Closest Binary Search Tree Value II ($$$)
Problem   : https://leetcode.com/problems/closest-binary-search-tree-value-ii/description/
          : https://www.lintcode.com/problem/closest-binary-search-tree-value-ii/description
'''
# Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
'''
iterative solution, comparing while searching down the BST in ascending order
Reference: https://www.jasonjson.com/archivers/closest-binary-search-tree-value-ii.html
'''
class Solution:    
    def closestKValues(self, root, target, k):
        if not root: return []
        stack, res, node = [], [], root
        while stack or node:
            if node:
                stack.append(node)
                node = node.left
            else:
                node = stack.pop()
                if len(res) < k:
                    res.append(node.val)
                elif abs(node.val - target) < abs(res[0] - target):   # DFS appending ensures that res is in ascending order thus only need to check the first element
                    del res[0]
                    res.append(node.val)
                else:
                    break
                node = node.right
        return res

''' recursive helper function exhausting all nodes + min heap to store (difference, node.val) in order '''
import heapq
class Solution:
    def closestKValues(self, root, target, k):
        if not root: return []
        heap = []
        heapq.heapify(heap)
        heap = self.helper(root, target, heap)
        count, res = 0, []
        while len(heap) != 0 and count < k:
            res.append(heapq.heappop(heap)[1])
            count += 1
        return res
        
    def helper(self, root, target, heap):
        if root:
            heapq.heappush(heap, (abs(target-root.val), root.val))
            heap = self.helper(root.left, target, heap)
            heap = self.helper(root.right, target, heap)
        return heap