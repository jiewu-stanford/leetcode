'''
Title     : 207. Course Schedule
Problem   : https://leetcode.com/problems/course-schedule/
'''
'''
translated into graph the criterion of completion is translated into whether there exists a cycle passing through it or not
DFS solution with three instead of two states: 0 = unvisited, 1 = visiting/in current traversal, 2 = visited/dfs check completed
Reference: https://leetcode.com/problems/course-schedule/discuss/58586/Python-20-lines-DFS-solution-sharing-with-explanation
Video (Chinese): https://www.youtube.com/watch?v=M6SBePBMznU
'''
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = [[] for _ in range(numCourses)]
        visited = [0 for _ in range(numCourses)]
        for course, prereq in prerequisites:
            graph[course].append(prereq)
        for i in range(numCourses):
            if not self.helper(graph, visited, i):
                return False
        return True
    
    def helper(self, graph, visited, i):
        if visited[i] == 2:
            return True
        elif visited[i] == 1:   # is being checked by dfs thus contained in current traversal hence form a cycle
            return False
        else:
            visited[i] = 1
            for j in graph[i]:
                if not self.helper(graph, visited, j):
                    return False
            visited[i] = 2   # dfs check completed and no cycle detected on all neighbors
            return True 
'''
topological sort based on in-degree (= number of inbounds) defined as number of prerequisites
Reference: https://leetcode.com/problems/course-schedule/discuss/58537/AC-Python-topological-sort-52-ms-solution-O(V-%2B-E)-time-and-O(V-%2B-E)-space
Video (Chinese): https://www.youtube.com/watch?v=fskPWs3Nuhc
'''
import collections
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = {i: set() for i in range(numCourses)}
        inDeg = {i: 0 for i in range(numCourses)}
        for course, prereq in prerequisites:
            graph[prereq].add(course)
            inDeg[course] += 1
        
        queue = collections.deque([i for i,deg in inDeg.items() if deg==0])
        visited = set()
        while queue:
            p = queue.popleft()
            visited.add(p)
            for c in graph[p]:
                inDeg[c] -= 1   # one fewer inbound if prerequisite p of course c is taken out
                if inDeg[c] == 0:
                    queue.append(c)
        
        return len(visited) == numCourses
'''
same idea but use stack instead of queue, inbounds dictionary instead of in-degree dictionary
Reference: https://leetcode.com/problems/course-schedule/discuss/58793/Short-Python-Topological-Sort
'''
import collections
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = collections.defaultdict(set)
        inbounds = collections.defaultdict(set)
        for course, prereq in prerequisites:
            graph[prereq].add(course)
            inbounds[course].add(prereq)
            
        stack = [n for n in range(numCourses) if not inbounds[n]]   # queue = collections.deque([i for i,deg in inDeg.items() if deg==0])
        count = 0   # visited = set()
        while stack:
            p = stack.pop()
            count += 1
            for c in graph[p]:
                inbounds[c].remove(p)
                if not inbounds[c]:
                    stack.append(c)
                    
        return count == numCourses