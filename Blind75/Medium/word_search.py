board = [["A","B","C","E"],
         ["S","F","C","S"],
         ["A","D","E","E"]] 

word = ""


def wordSearch(grid, word):
    def dfs(row, col, k):
        if k == len(word):
            return True
        
        if row<0 or row>=len(grid) or col<0 or col>=len(grid[0]) or grid[row][col]!=word[k]:
            return False
        
        temp, grid[row][col] = grid[row][col], "**" #mark visited
        res = dfs(row+1, col, k+1) or dfs(row-1, col, k+1) or dfs(row, col+1, k+1) or dfs(row, col-1, k+1)
        grid[row][col] = temp
        return res


    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if dfs(i, j, 0):
                return True
    return False


res = wordSearch(board, word)
print(res)