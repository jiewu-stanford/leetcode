'''
Title     : 399. Evaluate Division
Problem   : https://leetcode.com/problems/evaluate-division/
'''
'''
BFS helper function and build directed graph with quotient as the edge value
Reference: https://leetcode.com/problems/evaluate-division/discuss/88275/Python-fast-BFS-solution-with-detailed-explantion
'''
from collections import defaultdict, deque
class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        graph = defaultdict(dict)
        for ((x,y),val) in zip(equations, values):
            graph[x][y] = val   # x is dividend, y is divisor, x / y = val
            graph[y][x] = 1/val

        def helper(x, y):
            if x not in graph or y not in graph: return -1.0
            if x == y: return 1.0
            queue = deque([(x, 1.0)])
            visited = {x}
            while queue:
                z, curr = queue.popleft()
                for child, val in graph[z].items():
                    if child in visited: continue
                    nval = curr * val   # (x / z = curr) & (z / child = val) -> x / child = curr * val
                    if child == y: return nval
                    graph[x][child] = nval
                    graph[child][x] = 1/nval
                    visited.add(child)
                    queue.append((child, nval))
            return -1.0

        return [helper(x,y) for [x,y] in queries]
'''
variant of Floyd-Warshall algorithm (https://www.youtube.com/watch?v=4OQeCuLYj-4) without shortest path update
Reference: https://leetcode.com/problems/evaluate-division/discuss/88175/9-lines-%22Floydu2013Warshall%22-in-Python
'''
from collections import defaultdict, deque
class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        quot = defaultdict(dict)
        for (num, den), val in zip(equations, values):   # num(erator) / den(ominator) = val
            quot[num][num] = quot[den][den] = 1.0
            quot[num][den] = val
            quot[den][num] = 1 / val
        
        for k in quot:
            for i in quot[k]:
                for j in quot[k]:
                    quot[i][j] = quot[i][k] * quot[k][j]
        
        return [quot[num].get(den, -1.0) for num, den in queries]