'''
Title     : 379. Design Phone Directory ($$$)
Problem   : https://leetcode.com/problems/design-phone-directory/
'''
''' Reference: http://fernisoites.blogspot.com/2016/08/379-design-phone-directory.html '''

class PhoneDirectory(object):

    def __init__(self, maxNumbers):
        """
        Initialize your data structure here
        @param maxNumbers - The maximum numbers that can be stored in the phone directory.
        :type maxNumbers: int
        """
        self.maxNumbers = maxNumbers
        self.used = set()
        self.available = set()
        for i in range(maxNumbers):
            self.available.add(i)

    def get(self):
        """
        Provide a number which is not assigned to anyone.
        @return - Return an available number. Return -1 if none is available.
        :rtype: int
        """
        if self.available:
            num = self.available.pop()
            self.used.add(num)
            return num
        else:
            return -1

    def check(self, number):
        """
        Check if a number is available or not.
        :type number: int
        :rtype: bool
        """
        if number not in self.available: return False
        else: return True

    def release(self, number):
        """
        Recycle or release a number.
        :type number: int
        :rtype: void
        """
        if number >= self.maxNumbers: return
        elif number in self.used:
            self.used.remove(number)
            self.available.add(number)