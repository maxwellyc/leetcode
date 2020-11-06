def exist(board, word):
    m,n,l = len(board),len(board[0]),len(word)
    # b is complex number board
    stack,b,i = [],{},0
    for i in range(m):
        for j in range(n):
            b[i+j*1j] = board[i][j]
            if board[i][j] == word[0]:
                stack.append(i+j*1j)
    if l == 1 and stack: return True
    # backtrack
    def helper(z,w):
        if not w: return True
        for k in range(4):
            c = z+1j**(k+1)
            if c in b and b[c] == w[0]:
                b[c] = ''
                return helper(c,w[1:])
                b[c] = w[0]

    for z in stack:
        if helper(z,word[1:]):
            return True
    return False

board = [
  ['A','B','C','E'],
  ['S','F','C','S'],
  ['A','D','E','E']
]
word = "ABCCED"

print (exist(board,word))
