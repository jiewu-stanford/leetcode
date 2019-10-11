'''
Title     : 279. Perfect Squares
Problem   : https://leetcode.com/problems/perfect-squares/
'''
'''
1D DP solution where dp[i] = least number of perfect square summands for i, slow but clear
Reference: https://leetcode.com/problems/perfect-squares/discuss/275311/Python-DP-and-BFS
'''
class Solution:
    def numSquares(self, n: int) -> int:
        dp = [float('inf')]*(n+1)
        dp[0] = 0
        for i in range(1, n+1):
            dp[i] = min(dp[i-j*j] for j in range(1,int(i**0.5)+1)) + 1   # +1 represents adding the perfect square j*j
        return dp[n]
'''
BFS solution, reducing n to zero via successive subtraction of perfect squares (shortest path down a tree through perfect square nodes)
Reference: https://leetcode.com/problems/perfect-squares/discuss/71475/Short-Python-solution-using-BFS
'''
class Solution:
    def numSquares(self, n: int) -> int:
        if n < 2: return n
        squares = [i**2 for i in range(1, int(n**0.5)+1)]
        depth, nodes = 0, {n}
        while nodes:
            depth += 1
            tmp = set()
            for num in nodes:
                for sq in squares:
                    if num == sq:
                        return depth
                    elif num < sq:
                        break
                    else:
                        tmp.add(num - sq)
            nodes = tmp
        return depth