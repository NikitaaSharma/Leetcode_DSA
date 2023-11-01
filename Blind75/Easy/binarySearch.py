array = [2,4,6,8,12,24,37,57,89]
target = 45


def binarySearch(nums, tar):
    start = 0
    end = len(nums) - 1

    while start <= end:
        mid = start + (end-start) //2
        if nums[mid] > tar:
            end = mid -1
        elif nums[mid] < tar:
            start = mid + 1
        else:
            return mid
        
    return -1
        
    
res = binarySearch(array, target)
print(res)