"""
Q: Remove Duplicate from a sorted array in-place and return the number of unique elements

"""

def removeDuplicates(array):
    if not array:
        return 0
    
    j = 0
    for i in range(1, len(array)):
        if array[j] != array[i]:
            j +=1
            array[j] = array[i]

    return j+1

array = [0,0,0,1,1,1,2,2,3,3,3,3,4,4,5]
res = removeDuplicates(array)
print(f'{res} unique elements')