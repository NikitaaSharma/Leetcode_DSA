"""
Print the kth row of the Pascals triangle
for k = 3
1 3 3 1
"""

def pascalsKthRow(k):
    res_row = []
    res_row.append(1)
    if k == 0:
        print(res_row)
        return res_row

    prev_row = pascalsKthRow(k-1)

    for i in range(1, len(prev_row)):
        curr_row_val = prev_row[i-1] + prev_row[i]
        res_row.append(curr_row_val)

    res_row.append(1)
    print(res_row)
    return res_row

res = pascalsKthRow(6)
print(res)



