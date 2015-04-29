# Define Data Structure
n = 4
board = []

# Board Actions
def init_board():
    global board
    global n
    for i in range(n):
        b = []
        for j in range(n):
            b.append(0)
        board.append(b)

    for i in range(n):
        b = [0] * n
        board.append(b)

def print_board():
    # print board[n/2][n/2]
    global board
    global n

    for i in range(n):
        print '\t',
        for j in range(n):
            #  print board[i][j],
            if board[i][j] == 0:
                print '0',
            if board[i][j] == 1:
                print 'X',
            if board[i][j] == 2:
                print 'O',
        print ''

# Main code
init_board()

game_ended = False
while not game_ended:
    x = int(raw_input())
    y = int(raw_input())
    board[x - 1][y - 1] = 1
    print_board()
    print ''










