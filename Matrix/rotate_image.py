matrix= [[0,1,2,0],
         [2,3,4,5],
         [6,7,8,9],
         [10,11,12,13]]

for i in matrix:
    for j in i:
        print(j, end= " ")
    print(" ")
print("----------------------")
# always going to be square matrix, just reverse the matrix and transpose it

top_layer = 0
bottom_layer = len(matrix) - 1

while top_layer < bottom_layer:
    matrix[top_layer], matrix[bottom_layer] = matrix[bottom_layer], matrix[top_layer]
    top_layer +=1
    bottom_layer -=1

# transpose it

for row in range(len(matrix)):
    for col in range(row): #as row and col are same
        matrix[row][col], matrix[col][row] = matrix[col][row], matrix[row][col]

for i in matrix:
    for j in i:
        print(j, end= " ")
    print(" ")
