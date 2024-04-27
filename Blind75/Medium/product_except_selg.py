"""
Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].

The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

You must write an algorithm that runs in O(n) time and without using the division operation.

Sol: create a left side and a right side array, multiply both in the end
"""

def productExceptSelf(nums):
    n = len(nums)
    left_side = [1] * n
    right_side = [1] * n

    for i in range(1, n):
        left_side[i] = left_side[i-1] * nums[i-1]

    print(left_side)

    for i in range(n-2, -1, -1):
        right_side[i] = right_side[i+1] * nums[i+
        1]

    print(right_side)

    res = []
    for i in range(n):
        res.append(left_side[i] * right_side[i])

    return res

nums = [2,1,3,4]
res = productExceptSelf(nums)
print(res)