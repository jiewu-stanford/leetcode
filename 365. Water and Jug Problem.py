'''
Title     : 365. Water and Jug Problem
Problem   : https://leetcode.com/problems/water-and-jug-problem/
'''
'''
BFS + deque() solution detailing the moves, nonetheless TLE
Reference: https://leetcode.com/problems/water-and-jug-problem/discuss/83709/breadth-first-search-with-explanation
'''
from collections import deque
class Solution:
    def canMeasureWater(self, x: int, y: int, z: int) -> bool:
        if x + y < z: return False
        visited, queue = set(), deque([(0, 0)])
        while queue:
            i, j = queue.popleft()
            visited.add((i, j))
            if i + j == z:
                return True
            moves = set([(x,j), (i,y), (0,j), (i,0),
                        (min(i+j,x), (i+j)-min(i+j,x)),
                        ((i+j)-min(i+j,y), min(i+j,y)),])   # all possible next moves
            queue.extend(moves - visited)   # avoid going back to reached state
        return False

''' theory: https://leetcode.com/problems/water-and-jug-problem/discuss/83714/A-little-explanation-on-GCD-method.-C%2B%2BJavaPython '''
class Solution:
    def canMeasureWater(self, x: int, y: int, z: int) -> bool:
        from fractions import gcd
        return z == 0 or (x + y >= z and z % gcd(x, y) == 0)