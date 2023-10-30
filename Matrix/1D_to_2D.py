arr1d = [1,2,3,4,5,6,7,8]

def construct2DArray(array, m, n):
    ans = []
    if len(array) == m*n:
        for i in range(0, len(array), n):
            ans.append(array[i:i+n])

    return ans 

twoDArray = construct2DArray(arr1d, 4, 2)
print(twoDArray)
