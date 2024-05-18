"""
Largest contigous sum in an array: Kadane's Algo
"""
def largestContigousSum(nums):
    max_till_this_index = 0
    max_sum = float("-inf")

    for i in range(len(nums)):
        max_till_this_index = max_till_this_index + nums[i]
        if max_till_this_index > max_sum:
            max_sum = max_till_this_index
        if max_till_this_index < 0:
            max_till_this_index = 0
    return max_sum

arr = [4, -6, -2, 5]
res = largestContigousSum(arr)
print(res)