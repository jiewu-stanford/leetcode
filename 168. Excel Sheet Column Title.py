'''
Title     : 168. Excel Sheet Column Title
Problem   : https://leetcode.com/problems/excel-sheet-column-title/
'''
'''
straightforward recursive solution
Reference: https://leetcode.com/problems/excel-sheet-column-title/discuss/51398/My-1-lines-code-in-Java-C%2B%2B-and-Python
'''
class Solution:
    def convertToTitle(self, n: int) -> str:
        return '' if n == 0 else self.convertToTitle((n-1)//26) + chr((n-1)%26 + ord('A'))

''' iterative solution spelling out the same steps as in recursive solution '''
class Solution:
    def convertToTitle(self, n: int) -> str:
        res = []
        while n > 0:
            res = [chr((n-1)%26 + ord('A'))] + res
            n = (n-1) // 26
        return ''.join(res)