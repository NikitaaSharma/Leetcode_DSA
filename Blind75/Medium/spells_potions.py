"""
link: https://leetcode.com/problems/successful-pairs-of-spells-and-potions
"""

def search(spell, potions, success):
    start = 0
    end = len(potions) - 1
    ans = -1
    while start <= end:
        mid = start + (end- start) // 2
        if spell * potions[mid] >= success:
            ans = mid
            end = mid - 1
        else:
            start = mid + 1

    return ans

def successfulpair(spells, potions, success):
    potions.sort()
    res = []
    for spell in spells:
        success_count = 0
        index = search(spell, potions, success)
        if index == -1:
            success_count += 0
        else:
            success_count += len(potions) - index
        res.append(success_count)
    return res


spells = [5,1,3]
potions = [1,2,3,4,5]
success = 7

output = successfulpair(spells, potions, success)
print(output)