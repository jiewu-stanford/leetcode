'''
Title     : 210. Course Schedule II
Problem   : https://leetcode.com/problems/course-schedule-ii/
'''
'''
DFS solution using stack, directly adapted from the 207. solution
Reference: https://leetcode.com/problems/course-schedule-ii/discuss/59321/Python-dfs-bfs-solutions-with-comments
'''
import collections
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = collections.defaultdict(set)
        inbounds = collections.defaultdict(set)
        for course, prereq in prerequisites:
            graph[prereq].add(course)
            inbounds[course].add(prereq)
            
        stack = [n for n in range(numCourses) if not inbounds[n]]
        res = []
        while stack:
            p = stack.pop()
            res.append(p)   # count += 1
            for c in graph[p]:
                inbounds[c].remove(p)
                if not inbounds[c]:
                    stack.append(c)
            inbounds.pop(p)   # remove p and its prerequisites
            
        return res if not inbounds else []

''' topological sort using queue, directly adapted from the 207. solution, ibid. '''
import collections
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = {i: set() for i in range(numCourses)}
        inDeg = {i: 0 for i in range(numCourses)}
        for course, prereq in prerequisites:
            graph[prereq].add(course)
            inDeg[course] += 1
        
        queue = collections.deque([i for i,deg in inDeg.items() if deg==0])
        res = []
        while queue:
            p = queue.popleft()
            res.append(p)
            for c in graph[p]:
                inDeg[c] -= 1
                if inDeg[c] == 0:
                    queue.append(c)
            del inDeg[p]
        
        return res if not inDeg else []

''' DFS recursive helper function for cycle detection, directly adapted from the 207. solution, ibid. '''
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = [[] for _ in range(numCourses)]
        visited = [0 for _ in range(numCourses)]
        res = []
        for course, prereq in prerequisites:
            graph[course].append(prereq)
        for i in range(numCourses):
            noCycle, res = self.helper(graph, visited, i, res)
            if not noCycle: return []
        return res
    
    def helper(self, graph, visited, i, res):
        if visited[i] == 2:
            return True, res
        elif visited[i] == 1:
            return False, []
        else:
            visited[i] = 1
            for j in graph[i]:
                noCycle, res = self.helper(graph, visited, j, res)
                if not noCycle: return False, []
            visited[i] = 2
            res.append(i)
            return True, res