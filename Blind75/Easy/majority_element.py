nums = [2,2,2,3,4,4,2,4,4]

def majorityElement(nums):
    count = 0
    candidate = 0

    for i in nums:
        if count == 0:
            candidate = i
        if i == candidate:
            count +=1
        else:
            count -=1

    return candidate

maj = majorityElement(nums)
print(maj)