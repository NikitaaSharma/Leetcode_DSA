moves = [[0,0],[1,1],[0,1],[0,2],[1,0],[2,0]]

# A always starts first

# Solution: a scores array with 8 spots, since there are 8 ways a player can win
# position 0,1,2 is for rows, 3,4,5 is for cols, 6 for primary diagonal, 7th for secondary diagonal
# whenever a position is encountered by A, add 1 to the position, if B add -1
# when all moves are done, check which scores position has 3 or -3

def tictactoeWinner(moves):
    scores = [0] * 8
    for index, (row, col) in enumerate(moves):
        if index % 2 == 0:
            x = 1
        else:
            x = -1

        scores[row] +=x
        scores[col + 3] +=x
        if row == col:
            scores[6] +=x
        if 2 - row == col:
            scores[7] +=x

    for score in scores:
        if score ==3:
            return "A"
        elif score == -3:
            return "B"
        
    return "Draw" if len(moves) == 9 else "Pending"

winner = tictactoeWinner(moves)
print(winner)