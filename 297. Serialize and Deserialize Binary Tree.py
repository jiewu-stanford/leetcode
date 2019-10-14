'''
Title     : 297. Serialize and Deserialize Binary Tree
Problem   : https://leetcode.com/problems/serialize-and-deserialize-binary-tree/description/
'''
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
'''
recursive solution
Reference: https://leetcode.com/problems/serialize-and-deserialize-binary-tree/discuss/74259/Recursive-preorder-Python-and-C%2B%2B-O(n)
'''
class Codec:
    def serialize(self, root):
        if not root: return ''
        def helper(node, vals):
            if node:
                vals.append(str(node.val))
                helper(node.left, vals)
                helper(node.right, vals)
            else:
                vals.append('X')
            return vals
        vals = helper(root, [])
        return ' '.join(vals)

    def deserialize(self, data):
        if not data: return None
        def helper(vals):
            val = next(vals)   # next() is equivalent to pop() for iterables
            if val == 'X': return None
            node = TreeNode(int(val))
            node.left = helper(vals)
            node.right = helper(vals)
            return node
        vals = iter(data.split())   # make it iterable
        return helper(vals)
'''
step-by-step BFS iterative solution using deque
Reference: https://leetcode.com/problems/serialize-and-deserialize-binary-tree/discuss/166904/Python-or-BFS-tm
'''
import collections
class Codec:
    def serialize(self, root):
        if not root: return ''
        queue = collections.deque([root])
        vals = []
        while queue:
            node = queue.popleft()   # node = stack.pop(0)
            if node:
                vals.append(str(node.val))
                queue.append(node.left)   # stack.append(node.left)
                queue.append(node.right)
            else:
                vals.append('X')
        return ','.join(vals)

    def deserialize(self, data):
        if not data: return None
        vals = data.split(',')
        root = TreeNode(int(vals[0]))
        queue = collections.deque([root])
        i = 1
        while queue:
            node = queue.popleft()
            if vals[i] is not 'X':
                node.left = TreeNode(int(vals[i]))
                queue.append(node.left)
            i += 1
            if vals[i] is not 'X':
                node.right = TreeNode(int(vals[i]))
                queue.append(node.right)
            i += 1
        return root
'''
step-by-step DFS iterative solution using stack, note that the given example uses BFS serialization but the OJ simply test deserialize(serialize) = identity map
Reference: https://leetcode.com/problems/serialize-and-deserialize-binary-tree/discuss/74260/Recursive-DFS-Iterative-DFS-and-BFS
'''
class Codec:
    def serialize(self, root):
        if not root: return ''
        stack, node = [], root
        vals = []
        while node or stack:
            if node:
                vals.append(str(node.val))
                stack.append(node)
                node = node.left
            else:
                vals.append('X')
                node = stack.pop()
                node = node.right
        return ','.join(vals)

    def deserialize(self, data):
        if not data: return None
        vals = data.split(',')
        root = TreeNode(int(vals[0]))
        stack, node = [root], root
        i = 1
        while stack:
            while vals[i] is not 'X':
                node.left = TreeNode(int(vals[i]))
                stack.append(node.left)
                node = node.left
                i += 1
            while i < len(vals) and vals[i] == 'X':
                node = stack.pop()
                i += 1
            if i < len(vals):
                node.right = TreeNode(int(vals[i]))
                stack.append(node.right)
                node = node.right
                i += 1
        return root
'''
convert it to a typical structure of json, and then use built-in function of json package
Reference: https://leetcode.com/problems/serialize-and-deserialize-binary-tree/discuss/74430/Tuplify-%2B-json-Python
'''
import json
class Codec:
    def serialize(self, root):
        def tuplify(root):
            return root and (root.val, tuplify(root.left), tuplify(root.right))
        return json.dumps(tuplify(root))
        
    def deserialize(self, data):
        def detuplify(t):
            if t:
                root = TreeNode(t[0])
                root.left = detuplify(t[1])
                root.right = detuplify(t[2])
                return root
        return detuplify(json.loads(data))
        
# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))