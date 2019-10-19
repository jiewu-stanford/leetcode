'''
Title     : 310. Minimum Height Trees
Problem   : https://leetcode.com/problems/minimum-height-trees/
'''
'''
since there can be at most two leaves in a MHT we can iteratively remove leaves and associated edges till there is 1 or 2 left, rather slow though
note that there can be at most 2 MHTs, which can be proved by contradiction:
suppose there are 3 MHTs with root a, b, c having the same path length for each other
if the shortest path is 1 length, that means it's a single MHT, 2 length means there exists a tree with smaller length than a-b-c
Reference: https://leetcode.com/problems/minimum-height-trees/discuss/76132/Iterative-remove-leaves-Python-solution
Graphical Illustration: https://leetcode.com/problems/minimum-height-trees/discuss/76055/Share-some-thoughts
'''
import collections
class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        d = collections.defaultdict(set)
        for u, v in edges:
            d[u].add(v)
            d[v].add(u)

        nodes = set(range(n))
        while len(nodes) > 2:
            leaves = set(node for node in nodes if len(d[node])==1)   # leaf is defined as having only one linked node
            nodes -= leaves
            for leaf in leaves:
                for node in d[leaf]:
                    d[node].remove(leaf)
        
        return list(nodes)
'''
BFS iteratively solution using queue, progressively approach from outer leaves to inner nodes, ref. graphical illustration of leaf-deletion solution above
Reference: https://leetcode.com/problems/minimum-height-trees/discuss/76140/Short-O(n)-time-O(n)-space-Python-solution-using-BFS
'''
class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n < 2: return [0]
        degrees = [0]*n
        graph = {x:[] for x in range(n)}
        for edge in edges:
            degrees[edge[0]] += 1
            degrees[edge[1]] += 1
            graph[edge[0]].append(edge[1])
            graph[edge[1]].append(edge[0])

        queue = [x for x in range(n) if degrees[x]==1]   # leaves
        res = []
        while queue:
            tmp = []
            res = queue[:]
            for leaf in queue:
                for i in graph[leaf]:
                    degrees[i] -= 1   # progressively approach the interior and look for nodes that will qualify as leaves once outer nodes are deleted
                    if degrees[i] == 1: tmp.append(i)
            queue = tmp

        return res
'''
the root of a MHT has to be the middle point (or middle points, again at most 2) of the longest path (to be proved)
Reference: https://leetcode.com/problems/minimum-height-trees/discuss/76052/Two-O(n)-solutions
'''
import collections
class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        d = collections.defaultdict(set)
        for u, v in edges:
            d[u].add(v)
            d[v].add(u)

        def maxPath(startnode, visited):   # recursive maximum length path finder
            visited.add(startnode)
            paths = [maxPath(i, visited) for i in d[startnode] if i not in visited]
            path = max(paths or [[]], key=len)
            path.append(startnode)   # add startnode back (since the construction starts from its neighbors)
            return path

        path = maxPath(0, set())
        path = maxPath(path[0], set())
        l = len(path)
        return path[(l-1)//2: l//2+1]   # passes all test cases but needs proof