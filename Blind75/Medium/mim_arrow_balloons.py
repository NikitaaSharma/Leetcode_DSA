"""
link: https://leetcode.com/problems/minimum-number-of-arrows-to-burst-balloons/description/
There are some spherical balloons taped onto a flat wall that represents the XY-plane. The balloons are represented as
a 2D integer array points where points[i] = [xstart, xend] denotes a balloon whose horizontal diameter stretches between
xstart and xend. You do not know the exact y-coordinates of the balloons.

Arrows can be shot up directly vertically (in the positive y-direction) from different points along the x-axis.
A balloon with xstart and xend is burst by an arrow shot at x if xstart <= x <= xend. There is no limit to the number
of arrows that can be shot. A shot arrow keeps traveling up infinitely, bursting any balloons in its path.

Given the array points, return the minimum number of arrows that must be shot to burst all balloons.
"""
def findMinArrowShots(points):
    # sort the ballons by their ending dia
    points.sort(key= lambda x:x[1])
    arrow_count = 0
    ending = float("-inf")

    for balloon in points:
        if balloon[0] > ending:
            arrow_count +=1
            ending = balloon[1]

    return arrow_count

points = [[10,16], [2,8], [1,6], [7,12]]
result = findMinArrowShots(points)

print(f'Min arrows to burst all {len(points)} balloons is: {result}')