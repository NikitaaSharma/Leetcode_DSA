"""
link: https://leetcode.com/problems/max-number-of-k-sum-pairs/description/
"""

def maxOperations(nums, k):
    nums.sort()
    left, right = 0, len(nums) - 1
    oper = 0

    while left < right:
        target = nums[left] + nums[right]
        if target == k:
            left +=1
            right -=1
            oper +=1
        elif target < k:
            left +=1
        else:
            right -=1

    return oper



nums = [3,1,3,4,3]
k = 6

ans = maxOperations(nums, k)
print(ans)
