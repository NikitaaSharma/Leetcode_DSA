nums = [-1,0,1,2,-1,-4]


def threeSum(nums):
    res = []
    nums.sort()

    for index, val in enumerate(nums):
        if index>0 and val == nums[index - 1]:
            continue

        left = index + 1
        right = len(nums) - 1

        while left < right:
            threeSum = val + nums[left] + nums[right]
            if threeSum > 0:
                right -=1
            elif threeSum < 0:
                left +=1
            else:
                res.append([val, nums[left], nums[right]])
                left +=1
                while left<right and nums[left] == nums[left-1]:
                    left+=1

    return res
    
res = threeSum(nums)
print(res)