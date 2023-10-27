# we need to delete the greatest value in each row and add that value to the sum

grid = [[1,2,4],
        [3,3,1]]


def deleteGreatestValue(grid):
    for i in range(len(grid)):
        grid[i].sort()

    print(grid)
    sum = 0
    col_len = len(grid[0])

    for j in range(col_len):
        max_element = 0
        for i in range(len(grid)):
            max_element = max(max_element, grid[i].pop())

        sum += max_element

    return sum


sum = deleteGreatestValue(grid)
print(sum)
