'''
Title     : 301. Remove Invalid Parentheses
Problem   : https://leetcode.com/problems/remove-invalid-parentheses/description/
'''
'''
iterative solution, BFS + deque(), BFS in the sense that every '(' and ')' is deleted to try whether the resulted string is valid
Reference: http://bookshadow.com/weblog/2015/11/05/leetcode-remove-invalid-parentheses/
'''
import collections
class Solution:
    def removeInvalidParentheses(self, s: str) -> List[str]:
        res, visited = [], set([s])
        queue = collections.deque([s])
        done = False
        while queue:
            substr = queue.popleft()
            if self.isValid(substr):
                done = True
                res.append(substr)
            if done: continue   # we only want the minimum number of removal thus the execution of the for loop below only once
            for i in range(len(substr)):
                if substr[i] not in ('(', ')'): continue
                newstr = substr[:i] + substr[i+1:]
                if newstr not in visited:
                    queue.append(newstr)
                    visited.add(newstr)                    
        return res

    def isValid(self, s):
        count = 0
        for c in s:
            if c == '(': count += 1
            elif c == ')':
                count -= 1
                if count < 0: return False
        return count == 0

''' use a more intelligent helper function for BFS so that delete only if it can reduce the number of unpaired parentheses '''
import collections
class Solution:
    def removeInvalidParentheses(self, s: str) -> List[str]:
        res, visited = [], set([s])
        queue = collections.deque([s])
        done = False
        while queue:
            substr = queue.popleft()
            if not self.unpaired(substr):
                done = True
                res.append(substr)
            if done: continue
            for i in range(len(substr)):
                if substr[i] not in ('(',')'): continue
                newstr = substr[:i] + substr[i+1:]
                if newstr not in visited and self.unpaired(newstr) < self.unpaired(substr):
                    queue.append(newstr)
                    visited.add(newstr)
        return res
    
    def unpaired(self, s):
        a = b = 0
        for c in s:
            if c == '(': a += 1
            elif c == ')':
                a -= 1
                if a < 0: b += 1; a = 0
        return a + b

''' DFS recursive helper function, the enforcement of minimum is implicit through DFS though, ibid. '''
import collections
class Solution:
    def removeInvalidParentheses(self, s: str) -> List[str]:
        visited = set([s])
        def helper(substr):
            if not self.unpaired(substr):
                return [substr]
            res = []
            for i in range(len(substr)):
                if substr[i] not in ('(',')'): continue
                newstr = substr[:i] + substr[i+1:]
                if newstr not in visited and self.unpaired(newstr) < self.unpaired(substr):
                    res.extend(helper(newstr))
                    visited.add(newstr)
            return res
        return helper(s)
    
    def unpaired(self, s):
        a = b = 0
        for c in s:
            if c == '(': a += 1
            elif c == ')':
                a -= 1
                if a < 0: b += 1; a = 0
        return a + b