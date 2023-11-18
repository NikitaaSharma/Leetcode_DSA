"""
link: https://leetcode.com/problems/container-with-most-water/description/

You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of
the ith line are (i, 0) and (i, height[i]).

Find two lines that together with the x-axis form a container, such that the container contains the most water.

Return the maximum amount of water a container can store.

"""

def mostWater(height):
    ans, left, right = 0, 0, len(height) - 1

    while left < right:
        if height[left] <= height[right]:
            res = height[left] * (right - left)
            left+=1
        else:
            res = height[right] * (right - left)
            right -=1

        if res > ans: ans = res
    return ans


height = [1,8,6,2,5,4,8,3,7]
res = mostWater(height)
print(f"Most water contained is {res}")