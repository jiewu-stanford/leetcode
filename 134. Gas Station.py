'''
Title     : 134. Gas Station
Problem   : https://leetcode.com/problems/gas-station/
'''
''' straightforward iterative solution tracing out the path, note that cyclicity is easily handled with % L '''
class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        L = len(gas)
        if (sum(gas) - sum(cost)) < 0: return -1
        tank, start, curr = 0, 0, 0
        while True:
            tank += gas[curr]
            if tank - cost[curr] < 0:
                tank = 0
                start = (curr + 1) % L
                curr = start
                continue
            tank -= cost[curr]
            curr = (curr + 1) % L
            if start == curr:
                return start
'''
use the given fact that the solution if exists should be unique, find the station with lowest (thus unique) cumulative (gas - cost)
Reference: https://leetcode.com/problems/gas-station/discuss/42673/AC-Python-O(n)-time-O(1)-space-one-pass-8-lines
'''
class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        L = len(gas)
        if (sum(gas) - sum(cost)) < 0: return -1
        tank, start, tank_min = 0, 0, gas[0]
        for i in range(L):
            tank += gas[i] - cost[i]
            if tank < tank_min:
                tank_min = tank
                start = i
        return (start + 1) % L if tank >= 0 else -1