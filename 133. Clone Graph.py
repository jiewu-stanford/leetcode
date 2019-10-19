'''
Title     : 133. Clone Graph
Problem   : https://leetcode.com/problems/clone-graph/
'''
'''
DFS recursive solution using dictionary to record copies
Reference: https://leetcode.com/problems/clone-graph/discuss/42314/Python-solutions-(BFS-DFS-iteratively-DFS-recursively).
'''
# Definition for a Node.
class Node:
    def __init__(self, val, neighbors):
        self.val = val
        self.neighbors = neighbors

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        d = {}
        def helper(node):
            if not node: return
            node_copy = Node(node.val, [])
            d[node] = node_copy
            for neighbor in node.neighbors:
                if neighbor in d:
                    node_copy.neighbors.append(d[neighbor])
                else:
                    node_copy.neighbors.append(helper(neighbor))
            return node_copy
        return helper(node)

''' DFS iterative solution using stack to spell out the recursive steps, ibid. '''
class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node: return
        node_copy = Node(node.val, [])
        d = {node: node_copy}
        stack = [node]   # stack to maintain nodes the neighbors of whose copy are yet to be determined
        while stack:
            node = stack.pop()
            for neighbor in node.neighbors:
                if neighbor in d:
                    d[node].neighbors.append(d[neighbor])
                else:
                    neighbor_copy = Node(neighbor.val, [])
                    d[neighbor] = neighbor_copy
                    d[node].neighbors.append(neighbor_copy)
                    stack.append(neighbor)
        return node_copy

''' BFS iterative solution using queue, ibid. '''
import collections
class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node: return
        node_copy = Node(node.val, [])
        d = {node: node_copy}
        queue = collections.deque([node])
        while queue:
            node = queue.popleft()
            for neighbor in node.neighbors:
                if neighbor in d:
                    d[node].neighbors.append(d[neighbor])
                else:
                    neighbor_copy = Node(neighbor.val, [])
                    d[neighbor] = neighbor_copy
                    d[node].neighbors.append(neighbor_copy)
                    queue.append(neighbor)
        return node_copy