'''
Title     : 332. Reconstruct Itinerary
Problem   : https://leetcode.com/problems/reconstruct-itinerary/description/
'''
'''
DFS solution with recursive helper function
Reference: https://leetcode.com/problems/reconstruct-itinerary/discuss/78772/Python-Dfs-Backtracking
'''
import collections
class Solution(object):
    def findItinerary(self, tickets):
        d = collections.defaultdict(list)
        for start, end in tickets:
            d[start] += end,   # , to convert non-iterable string to iterable tuple
        self.route = ['JFK']

        def helper(start='JFK'):
            if len(self.route) == len(tickets)+1:
                return self.route
            destinations = sorted(d[start])   # sort to ensure lexicographically minimal
            for dst in destinations:
                d[start].remove(dst);   self.route += dst,
                itinerary = helper(dst)
                if itinerary:
                    return itinerary
                else:
                    self.route.pop();   d[start] += dst,   # if not able to concatenate then restore dictionary and try the next dst               

        return helper()
'''
iterative solution with stack, using the property of Eulerian path---there must be a start node and an end node
so the algorithm is to find the end node first and delete the path to it one step by one step (ref. TCoherence's comment)
Reference: https://leetcode.com/problems/reconstruct-itinerary/discuss/78768/Short-Ruby-Python-Java-C%2B%2B
'''
import collections
class Solution(object):
    def findItinerary(self, tickets):
        d = collections.defaultdict(list)
        for start, end in sorted(tickets)[::-1]:   # sort to ensure lexicographically minimal
            d[start] += end,
        route, stack = [], ['JFK']
        while stack:
            while d[stack[-1]]:
                stack.append(d[stack[-1]].pop())
            route.append(stack.pop())
        return route[::-1]