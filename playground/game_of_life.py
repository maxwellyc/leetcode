def gameOfLife(board):
    """
    Do not return anything, modify board in-place instead.
    """
    m = len(board)
    n = len(board[0])
    
    def count_nb(i,j):
        count = 0
        for a in range(-1,2):
            for b in range(-1,2):
                if -1<i+a<m and -1<j+b<n:
                    if board[i+a][j+b]>0:
                        count+=1
        return count-board[i][j]
    # live->dead = 2; dead->live = -1
    # live->live = 1; dead->dead = 0
    for i in range(m):
        for j in range(n):
            c = board[i][j]
            nb = count_nb(i,j)
            print (i,j,nb)
            # live cell
            if c and (nb<2 or nb>3):
                c = 2
            elif not c and nb == 3:
                c = -1
    for i in range(m):
        for j in range(n):
            c = board[i][j]
            if c == 2:
                board[i][j] = 0
            elif c == -1:
                board[i][j] = 1

board = [[0,1,0],[0,0,1],[1,1,1],[0,0,0]]
gameOfLife(board)
print (board)
