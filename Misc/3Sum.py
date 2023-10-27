nums = [-1,0,1,2,-1,-4]

# find 3 numbers which will pair up to be 0, a+b+c=0, no duplicates allowed

def findThreeSum(nums):
    res = []

    nums.sort()

    for i, n in enumerate(nums):
        if i > 0 and n == nums[i-1]:
            continue

        left, right = i+1, len(nums) - 1

        while left < right:
            threeSum = n + nums[left] + nums[right]
            if threeSum >0:
                right -=1
            elif threeSum < 0:
                left +=1
            else:
                res.append([n, nums[left], nums[right]])
                left +=1
                while left < right and nums[left] == nums[left - 1]:
                    left+=1

    return res

res = findThreeSum(nums)
print(res)
