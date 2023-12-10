"""

link: https://leetcode.com/problems/find-peak-element
A peak element is an element that is strictly greater than its neighbors.

Given a 0-indexed integer array nums, find a peak element, and return its index. If the array contains multiple peaks,
return the index to any of the peaks.
You may imagine that nums[-1] = nums[n] = -∞. In other words, an element is always considered to be strictly greater
than a neighbor that is outside the array.
You must write an algorithm that runs in O(log n) time.
"""

def findPeakElement(nums):
    n = len(nums)
    if n == 1:
        return 0

    start = 0
    end = n - 1
    while start <= end:
        mid = start + (end-start) // 2
        #if mid is the first element
        if mid == 0:
            if nums[mid] > nums[mid + 1]:
                return mid
            else:
                end = mid - 1
        # if mid is the last element
        elif mid == n - 1:
            if nums[mid] > nums[mid - 1]:
                return mid
            else:
                start = mid + 1
        else:
            if nums[mid] > nums[mid + 1] and nums[mid] > nums[mid - 1]:
                return mid
            else:
                if nums[mid] < nums [mid + 1]:
                    start = mid + 1
                else:
                    end = mid - 1

    return -1

nums = [1,2,3,1]
res = findPeakElement(nums)
print(res)
