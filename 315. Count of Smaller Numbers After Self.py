'''
Title     : 315. Count of Smaller Numbers After Self
Problem   : https://leetcode.com/problems/count-of-smaller-numbers-after-self/description/
'''
'''
traverse backward and maintain a sorted array of visited numbers, the trick to realize is that
the index of the sorted subarray at which the next number should be inserted is exactly the number of numbers smaller than it (thanks to sorting)
Reference: https://leetcode.com/problems/count-of-smaller-numbers-after-self/discuss/76576/My-simple-AC-Java-Binary-Search-code
'''
class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        if not nums: return []
        sortedNums = []
        res = [0] * len(nums)
        for i in range(len(nums)-1,-1,-1):
            indx = self.binarySearch(sortedNums, nums[i])   # indx = bisect.bisect_left(sortedNums, nums[i]), use bisect_right produces error
            res[i] = indx
            sortedNums.insert(indx, nums[i])
        return res

    def binarySearch(self, sortedNums, target):
        if not sortedNums: return 0
        l, r = 0, len(sortedNums)-1
        while l <= r:
            mid = (l + r) // 2
            if sortedNums[mid] < target:
                l = mid + 1
            else:
                r = mid - 1
        return l
'''
traverse backward and built a BST, by the BST defining property all the numbers smaller to a given number are on its right
Reference: https://leetcode.com/problems/count-of-smaller-numbers-after-self/discuss/76587/Easiest-Java-solution
'''
class node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.count = 1

class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        if not nums: return []
        root = node(nums[-1])
        res = [0]
        for i in range(len(nums)-2, -1, -1):
            res.append(self.insertNode(nums[i], root))
        return res[::-1]

    def insertNode(self, val, root):
        count = 0
        while True:
            if val <= root.val:
                root.count += 1
                if not root.left:
                    root.left = node(val); break
                root = root.left
            else:
                count += root.count
                if not root.right:
                    root.right = node(val); break
                root = root.right
        return count
'''
same idea of using tree structure to count naturally, but use BIT (https://www.youtube.com/watch?v=4SNzC4uNmTA) instead of BST
Reference: https://leetcode.com/problems/count-of-smaller-numbers-after-self/discuss/76657/3-ways-(Segment-Tree-Binary-Indexed-Tree-Binary-Search-Tree)-clean-python-code
'''
class BIT(object):
    def __init__(self, n):
        self.sums = [0] * (n+1)
    def update(self, i, val):
        while i < len(self.sums):
            self.sums[i] += 1
            i += i & -i   # the position of the last bit '1' in binary form of i (https://stackoverflow.com/questions/15395317/meaning-of-bitwise-and-of-a-positive-and-negative-number)
    def sum(self, i):
        res = 0
        while i > 0:
            res += self.sums[i]
            i -= i & -i
        return res

class Solution:
    def countSmaller(self, nums):
        d = {val: indx for indx, val in enumerate(sorted(set(nums)))}
        tree, res = BIT(len(d)), []
        for i in range(len(nums)-1, -1, -1):
            res.append(tree.sum(d[nums[i]]))
            tree.update(d[nums[i]]+1, 1)   # value is index thus = 1 or number of repetitions, thus running sum = number of numbers smaller than it (for a sorted set)
        return res[::-1]
'''
the smaller numbers on the right of a number are exactly those that jump from its right to its left during a stable sort
Reference: https://leetcode.com/problems/count-of-smaller-numbers-after-self/discuss/76583/11ms-JAVA-solution-using-merge-sort-with-explanation
'''
class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        if not nums: return []
        n = len(nums)
        self.count = [0] * n
        self.mergesort(nums, list(range(n)), 0, n)   # range object does not support item assignment in python 3
        return self.count

    def mergesort(self, nums, indx, low, high):
        if low >= high - 1: return
        mid = (low + high) // 2
        self.mergesort(nums, indx, low, mid)
        self.mergesort(nums, indx, mid, high)
        self.merge(nums, indx, low, high)

    def merge(self, nums, indx, low, high):
        mid = (low + high) // 2
        i, j = low, mid
        rightToleft = 0
        newIndx = []
        while i < mid and j < high:
            if nums[indx[i]] > nums[indx[j]]:
                newIndx.append(indx[j])
                rightToleft += 1
                j += 1
            else:
                newIndx.append(indx[i])
                self.count[indx[i]] += rightToleft
                i += 1
        while i < mid:   # exhaust remaining left half after comparison with all right half numbers are done
            self.count[indx[i]] += rightToleft
            newIndx.append(indx[i])
            i += 1
        while j < high:
            newIndx.append(indx[j])
            j += 1
        indx[low:high] = newIndx
'''
a more concise version of merge sort
Reference: https://leetcode.com/problems/count-of-smaller-numbers-after-self/discuss/76584/Mergesort-solution
'''
class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        def mergesort(enum):
            mid = len(enum) // 2
            if mid:
                leftHf, rightHf = mergesort(enum[:mid]), mergesort(enum[mid:])
                m, n = len(leftHf), len(rightHf)
                i = j = 0
                while i < m or j < n:
                    if j == n or (i < m and leftHf[i][1] <= rightHf[j][1]):
                        enum[i+j] = leftHf[i]
                        smaller[leftHf[i][0]] += j   # > any number in rightHf[0:j] since rightHf is ascending
                        i += 1
                    else:
                        enum[i+j] = rightHf[j]
                        j += 1
            return enum

        if not nums: return []
        smaller = [0] * len(nums)
        mergesort(list(enumerate(nums)))
        return smaller
''' work only on the index, ibid. '''
class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        def sort(inds):
            half = len(inds) // 2
            if half:
                left, right = sort(inds[:half]), sort(inds[half:])
                for i in range(len(inds))[::-1]:
                    if not right or left and nums[left[-1]] > nums[right[-1]]:
                        smaller[left[-1]] += len(right)
                        inds[i] = left.pop()
                    else:
                        inds[i] = right.pop()
            return inds

        smaller = [0]*len(nums)
        sort(list(range(len(nums))))
        return smaller