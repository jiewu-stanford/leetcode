'''
Title     : 391. Perfect Rectangle
Problem   : https://leetcode.com/problems/perfect-rectangle/description/
'''
''' Reference: https://leetcode.com/problems/perfect-rectangle/discuss/87180/O(n)-solution-by-counting-corners-with-detailed-explaination '''
import collections
class Solution(object):
    def insertCorner(self, cornerMap, x, y, val):
        if (x,y) in cornerMap and (cornerMap[(x,y)] & val): return False   # boundary corner can only appear once thus & val yields False
        cornerMap[(x,y)] |= val
        return True

    def isRectangleCover(self, rectangles):
        minx = maxx = rectangles[0][0]
        miny = maxy = rectangles[0][1]
        cornerMap = collections.defaultdict(int)
        for x1, y1, x2, y2 in rectangles:   # bottom left = (x1, y1) = 1, bottom right = (x2, y1) = 2, top left = (x1, y2) = 4, top right = (x2, y2) = 8
            minx, maxx = min(minx, x1), max(maxx, x2)
            miny, maxy = min(miny, y1), max(maxy, y2)
            if not self.insertCorner(cornerMap, x1, y1, 1): return False
            if not self.insertCorner(cornerMap, x2, y1, 2): return False
            if not self.insertCorner(cornerMap, x1, y2, 4): return False
            if not self.insertCorner(cornerMap, x2, y2, 8): return False
        validCorner = {1, 2, 4, 8}
        validInterior = {3, 5, 10, 12, 15}   # four T-intersections {1|2, 1|4, 2|8, 4|8} and one crossing {1|2|4|8}
        for x, y in cornerMap:
            if x in (minx, maxx) and y in (miny, maxy):
                if cornerMap[(x,y)] not in validCorner:
                    return False
            else:
                if cornerMap[(x,y)] not in validInterior:
                    return False
        return True
'''
explicit checking of area sum
Reference: https://leetcode.com/problems/perfect-rectangle/discuss/87207/Short-Java-solution-with-explanation-(updated)
'''
class Solution(object):
    def overlap(self, key, cornerType):
        tmp = self.cornerMap.get(key, 0)
        if not tmp: tmp = cornerType
        elif tmp & cornerType: return True
        else: tmp |= cornerType
        self.cornerMap[key] = tmp
        return False

    def isRectangleCover(self, rectangles):
        if not rectangles: return False
        self.cornerMap = {}
        maxx = maxy = -(1 << 31)
        minx = miny = 1 << 31 - 1
        areasum = 0
        for x1, y1, x2, y2 in rectangles:   # bottom left = (x1, y1) = 1, bottom right = (x2, y1) = 2, top left = (x1, y2) = 4, top right = (x2, y2) = 8, as long as each correponds to bit '1' in a different position
            minx, maxx = min(minx, x1), max(maxx, x2)
            miny, maxy = min(miny, y1), max(maxy, y2)
            areasum += (x2 - x1) * (y2 - y1)
            if self.overlap((x1, y1), 1): return False
            if self.overlap((x2, y1), 2): return False
            if self.overlap((x1, y2), 4): return False
            if self.overlap((x2, y2), 8): return False
        count = 0
        for val in self.cornerMap.values():
            if val in [1,2,4,8]: count += 1
        return count == 4 and areasum == (maxx-minx)*(maxy-miny)