nums = [32,43,10,23,3]
target = 35

def twoSum(nums, target):
    prevMap = {}
    
    for i, value in enumerate(nums):
        diff = target - value
        if diff in prevMap:
            return [prevMap[diff], i]
        prevMap[value] = i

    return [-1,-1]

twosum = twoSum(nums, target)
print(twosum)