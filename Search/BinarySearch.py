nums = [10,12,13,16,19,23,45,56,78,89]
target = 78


def binary(nums, target):
    start = 0
    end = len(nums) -1
    while start <= end:
        mid = start + (end-start) //2
        if target < nums[mid]:
            end = mid -1
        elif target > nums[mid]:
            start = mid+1
        else:
            return mid

res = binary(nums, target)
print(f"{target} at index {res}")
