'''
Title     : 261. Graph Valid Tree ($$$)
Problem   : https://leetcode.com/problems/graph-valid-tree/
          : https://www.lintcode.com/en/old/problem/graph-valid-tree/#
'''
'''
any connected graph without simple cycles is a tree, thus the task is reduced to (1) check connectivity (2) detect the existence of cycle，below is the union find solution
Reference: https://www.cnblogs.com/lightwindy/p/8636516.html
'''
class Solution:
    def validTree(self, n, edges):
        root = [i for i in range(n)]
        for edge in edges:
            root1 = self.findRoot(root, edge[0])
            root2 = self.findRoot(root, edge[1])
            if root1 == root2:   # the two ends belong to the same union hence a cycle
                return False
            else:
                root[root1] = root2   # connected by an edge so that they belong to the same union
        return len(edges) == n - 1
        
    def findRoot(self, root, e):
        if root[e] == e:
            return e
        else:
            root[e] = self.findRoot(root, root[e])
            return root[e]

''' DFS solution with recursive helper function, ibid. '''
import collections
class Solution:
    def validTree(self, n, edges):
        d = collections.defaultdict(list)   # maintain a dictionary of connected nodes for each node
        for edge in edges:
            d[edge[0]].append(edge[1])
            d[edge[1]].append(edge[0])
        visited = [False]*n
        
        if not self.helper(0, -1, d, visited):
            return False
            
        for v in visited:   # if there is any not visited node then the graph is not connected and/or has cycles
            if not v: return False
        return True
        
    def helper(self, curr, parent, dic, visited):
        if visited[curr]: return False   # visit again, cycle exists
        visited[curr] = True
        for node in dic[curr]:
            if node != parent and not self.helper(node, curr, dic, visited):   # keep track of parent to avoid traversing back to it
                return False
        return True

''' BFS iterative solution, the check of connectivity and existence of cycle is combined into checking reachability (test case doesn't include a single cycle connecting all nodes), ibid. '''
import collections
class Solution:
    def validTree(self, n, edges):
        if len(edges) != n - 1: return False
        d = collections.defaultdict(list)
        for edge in edges:
            d[edge[0]].append(edge[1])
            d[edge[1]].append(edge[0])
            
        visited = {}
        queue = collections.deque([0])
        while queue:
            curr = queue.popleft()
            visited[curr] = True
            for node in d[curr]:
                if node not in visited:
                    visited[node] = True
                    queue.append(node)
                    
        return len(visited) == n  # for a tree the breadth search should be able to reach every node