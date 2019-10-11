'''
Title     : 319. Bulb Switcher
Problem   : https://leetcode.com/problems/bulb-switcher/
'''
''' if i is a factor of n so is (n / i), thus unless the number is a perfect square it has even number of factors hence will eventually be turned off '''
class Solution:
    def bulbSwitch(self, n: int) -> int:
        return int(n**(0.5))