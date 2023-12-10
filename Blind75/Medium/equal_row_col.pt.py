"""
link: https://leetcode.com/problems/equal-row-and-column-pairs/?envType=study-plan-v2&envId=leetcode-75

return the count of exactly same rows and cols
"""


def equalPairs(grid):
    pairings = {}
    count = 0
    n = len(grid)

    # populate the hashmap: key is the string of all row values, and value is the occurance of that row in the grid
    for row in grid:
        key = str(row)
        if key in pairings:
            pairings[key] +=1
        else:
            pairings[key] = 1

    # Start reading the column and check if the string of that column exists in hashmap already
    for col in range(n):
        cols = []
        for row in range(n):
            cols.append(grid[row][col])

        key = str(cols)
        if key in pairings:
            count += pairings[key]

    return count



grid = [[3,2,1],[1,7,6],[2,7,7]]
res=equalPairs(grid)
print(res)