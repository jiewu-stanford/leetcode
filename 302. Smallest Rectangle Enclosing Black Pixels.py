'''
Title     : 302. Smallest Rectangle Enclosing Black Pixels ($$$)
Problem   : https://leetcode.com/problems/smallest-rectangle-enclosing-black-pixels/description/
          : https://www.lintcode.com/problem/smallest-rectangle-enclosing-black-pixels/description
'''
'''
binary search for both row and column, use any() to check all rows for black pixel in a give column
Reference: https://github.com/csujedihy/lc-all-solutions/blob/master/302.smallest-rectangle-enclosing-black-pixels/smallest-rectangle-enclosing-black-pixels.py
'''
class Solution:
    """
    @param image: a binary matrix with '0' and '1'
    @param x: the location of one of the black pixels
    @param y: the location of one of the black pixels
    """
    def minArea(self, image, x, y):
        top = self.searchRow(image, 0, x, True)                 # True = going up/left (mid <-- j)
        bottom = self.searchRow(image, x+1, len(image), False)  # False = going down/right (i --> mid+1)
        left = self.searchCol(image, 0, y, top, bottom, True)
        right = self.searchCol(image, y+1, len(image[0]), top, bottom, False)
        return (right - left) * (bottom - top)

    def searchRow(self, image, i, j, option):
        while i < j:
            mid = (i + j) // 2
            if ('1' in image[mid]) == option:
                j = mid
            else:
                i = mid + 1
        return i

    def searchCol(self, image, i, j, top, bottom, option):
        while i < j:
            mid = (i + j) // 2
            if any([image[k][mid] == '1' for k in range(top, bottom)]) == option:
                j = mid
            else:
                i = mid + 1
        return i
'''
combine searchRow() and searchCol() into one single binary search with checking function
Reference: https://leetcode.com/discuss/68407/clear-binary-search-python
'''
class Solution:
    def minArea(self, image, x, y):
        top = self.searchs(image, 0, x, lambda mid: '1' in image[mid])
        bottom = self.searchs(image, x+1, len(image), lambda mid: '1' not in image[mid])
        left = self.searchs(image, 0, y, lambda mid: any(image[k][mid]=='1' for k in range(top, bottom)))
        right = self.searchs(image, y+1, len(image[0]), lambda mid: all(image[k][mid]=='0' for k in range(top, bottom)))   # all=='0' is the negation of any=='1'
        return (right - left) * (bottom - top)

    def searchs(self, image, i, j, checkfunction):
        while i < j:
            mid = (i + j) // 2
            if checkfunction(mid):
                j = mid
            else:
                i = mid + 1
        return i