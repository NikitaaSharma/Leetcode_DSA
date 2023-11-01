grid = [[4,3,2,-1],
        [3,2,1,-1],
        [1,1,-1,-1],
        [-1,-1,-2,-3]]

# Grid is sorted in descending order, find the number of negatives

# SOlution: Do binary search in each row and find the first negative number, since the row is sorted, all numbers after that
# would be -ve as well, therefore, -ve in that row = total elements - index (len(grid)) - i)

def countNegatives(grid):
    
    def bs(row):
        start = 0
        end = len(row) 
        while start <end:
            mid = start + (end-start) //2
            if row[mid] < 0:
                end =  mid
            else:
                start = mid + 1

        return len(row) - start

    
    count = 0
    for i in grid:
        count += bs(i)

    return count

res = countNegatives(grid)
print(res)