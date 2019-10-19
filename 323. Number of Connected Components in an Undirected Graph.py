'''
Title     : 323. Number of Connected Components in an Undirected Graph ($$$)
Problem   : https://leetcode.com/problems/number-of-connected-components-in-an-undirected-graph/description/
'''
"""
Given n nodes labeled from 0 to n - 1 and a list of undirected edges (each edge is a pair of nodes), write a function to find the number of connected components in an undirected graph.
e.g. Given n = 5 and edges = [[0, 1], [1, 2], [3, 4]], Solution().countComponents(5, [[0, 1], [1, 2], [3, 4]]) returns 2
     Given n = 5 and edges = [[0, 1], [1, 2], [2, 3], [3, 4]], Solution().countComponents(5, [[0, 1], [1, 2], [3, 4]]) returns 1
"""
'''
Reference: http://www.voidcn.com/article/p-alarubsd-qp.html
Reference: https://github.com/KrisYu/LeetCode-CLRS-Python/blob/master/323.%20Number%20of%20Connected%20Components%20in%20an%20Undirected%20Graph.md
Reference: https://www.cnblogs.com/lightwindy/p/8487160.html
'''
class Solution(object):
    def countComponents(self, n, edges):
        if not edges: return 0
        self.components = {i:i for i in range(n)}
        res = n
        for edge in edges:
            if self.unite(edge[0], edge[1]):
                res -= 1
        return res

    def unite(self, i, j):
        icomponent = self.findcomp(i)
        jcomponent = self.findcomp(j)
        if icomponent == jcomponent:
            return False
        else:
            self.components[min(icomponent, jcomponent)] = max(icomponent, jcomponent)   # min, max to avoid assignment ambiguity
            return True

    def findcomp(self, i):
        if self.components[i] != i:   # has been united with others
            self.components[i] = self.findcomp(self.components[i])
        return self.components[i]