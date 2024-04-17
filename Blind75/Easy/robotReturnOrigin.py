def returnToOrigin(moves):
    steps = 0
    if not moves.count('U') == moves.count('D'):
        steps +=1
    if not moves.count('R') == moves.count('L'):
        steps +=1
    return steps == 0

moves = 'UDRLLR'
res = returnToOrigin(moves)
print(res)