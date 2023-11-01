nums = [1,2,3,6]

def containsDuplicate(arr):
    hashSet = set()

    for i in nums:
        if i in hashSet:
            return True
        hashSet.add(i)
    return False

res = containsDuplicate(nums)
print(res)