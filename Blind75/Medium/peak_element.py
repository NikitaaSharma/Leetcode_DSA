"""

link: https://leetcode.com/problems/find-peak-element

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
