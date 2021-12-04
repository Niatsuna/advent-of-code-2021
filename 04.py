# >>> Read Input <<<
input = []
with open('inputs/04.txt', 'r') as f:
  f_ = f.readlines()
  input.append([int(x) for x in f_[0].strip().split(',')])
  i = 2
  while(i < len(f_)) :
    board = []
    for j in range(0,  5):
      board.append([int(x) for x in f_[i+j].strip().replace('  ',' ').split(' ')])

    i += 6
    input.append(board)

# >>> Solution - 1 <<<
print('=== PART ONE ===')
def checkBingoRow(board):
  for r in board:
    if r == ['X','X','X','X','X']:
      return True
  return False

def checkBingoCol(board):
  for c in range(0, 5):
    if [board[0][c], board[1][c], board[2][c], board[3][c], board[4][c]] == ['X','X','X','X','X']:
      return True
  return False
'''
def checkDiagonal(board):
  if [board[0][0], board[1][1], board[2][2], board[3][3], board[4][4]] == ['X','X','X','X','X']:
    return True

  if [board[4][0], board[3][1], board[2][2], board[1][3], board[0][4]] == ['X','X','X','X','X']:
    return True
  return False
'''

def checkBingo(board):
  return (checkBingoRow(board) or checkBingoCol(board))

def markDraw(board, draw):
  for r in range(0, 5):
    for c in range(0, 5):
      if board[r][c] == draw:
        board[r][c] = 'X'
        return

winner = False
for draw in input[0]:
  for board in input[1:]:
    markDraw(board, draw)
    if checkBingo(board):
      print(f'WE HAVE A WINNER WITH NUMBER {draw} !')

      count = 0
      for r in board:
        for c in r:
          if c != 'X':
            count += c
      print(f'Final Score: {count*draw}')

      winner = True
      break
  if winner:
    break

# >>> Solution - 2 <<<
print('=== PART TWO ===')
def checkBingoRow(board):
  for r in board:
    if r == ['X','X','X','X','X']:
      return True
  return False

def checkBingoCol(board):
  for c in range(0, 5):
    if [board[0][c], board[1][c], board[2][c], board[3][c], board[4][c]] == ['X','X','X','X','X']:
      return True
  return False
'''
def checkDiagonal(board):
  if [board[0][0], board[1][1], board[2][2], board[3][3], board[4][4]] == ['X','X','X','X','X']:
    return True

  if [board[4][0], board[3][1], board[2][2], board[1][3], board[0][4]] == ['X','X','X','X','X']:
    return True
  return False
'''

def checkBingo(board):
  return (checkBingoRow(board) or checkBingoCol(board))

def markDraw(board, draw):
  for r in range(0, 5):
    for c in range(0, 5):
      if board[r][c] == draw:
        board[r][c] = 'X'
        return

loser = False
delete = []
for draw in input[0]:
  for board in input[1:]:
    markDraw(board, draw)
    if checkBingo(board):
      if len(input[1:]) == 1:
        print(f'WE HAVE A LOSER WITH NUMBER {draw} !')
        count = 0
        for r in board:
          for c in r:
            if c != 'X':
              count += c
        print(f'Final Score: {count*draw}')
        loser = True
        break
      input.remove(board)
  if loser:
    break

