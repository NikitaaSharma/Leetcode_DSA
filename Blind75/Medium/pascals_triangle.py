"""
link: https://leetcode.com/problems/pascals-triangle/description/
print pascals triangle based on numRows given
"""

def printPascalsTriangle(numRows):
    triangle = [[1]]
    if numRows == 0:
        return []

    for i in range(1, numRows):
        prev_row = triangle[-1]
        curr_row = [1]

        for j in range(1, len(prev_row)):
            curr_row.append(prev_row[j-1] + prev_row[j])

        curr_row.append(1)

        triangle.append(curr_row)
    return triangle


tri = printPascalsTriangle(5)
print(tri)