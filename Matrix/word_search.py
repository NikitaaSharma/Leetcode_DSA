board = [["A","B","C","E"],
         ["S","F","C","S"],
         ["A","D","E","E"]] 

word = "SAD"

# we will use DFS here, basically start with the first letter of the word, perform DSA up until we arrive at the last letter, if
# the k+1th letter is not found till the end, return False. Search for the adjacent row (up and down) and adjacent column (up& down).

def Solution(board, word):
    def dfs(row, col, k):
        if k == len(word):
            return True
        
        if row<0 or row>=len(board) or col<0 or col>=len(board[0]) or board[row][col] != word[k]:
            return False
        
        #mark the visited cell with something
        temp, board[row][col] = board[row][col], "**"
        result = dfs(row+1, col, k+1) or dfs(row-1, col, k+1) or dfs(row, col+1, k+1) or dfs(row, col-1, k+1)
        board[row][col] = temp
        return result

    for row in range(len(board)):
        for col in range(len(board[0])):
            if dfs(row, col, 0):
                return True
            
        
    return False

print(Solution(board, word))