"""
link: https://leetcode.com/problems/koko-eating-bananas
"""
import math


def minEatingSpeed(piles, h):
    ans = 0
    # min speed possible
    start = 1
    # max no. of bananas in the pile
    end = max(piles)

    # return true if it is possible to eat all the bananas before the guards come back
    def isPossible(mid, piles, h):
        hours_to_eat = 0
        for i in piles:
            # round up the hour
            hours_to_eat += math.ceil(i/mid)

        return hours_to_eat <= h


    while start <= end:
        mid = start + (end-start) // 2
        if isPossible(mid, piles, h):
            # narrow down the search to find the minimum speed
            ans = min(mid, end)
            end = mid - 1
        else:
            start = mid + 1

    return ans


piles = [30,11,23,4,20]
h = 5

out = minEatingSpeed(piles, h)
print(out)
