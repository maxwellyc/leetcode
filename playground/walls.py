import numpy as np
def wallsAndGates(rooms):
    """
    Do not return anything, modify rooms in-place instead.
    """
    m = len(rooms)
    print('\n'.join([''.join(['{:4}'.format(item) for item in row])
      for row in rooms]))
    print ("output:")
    if m>0:
        n = len(rooms[0])
        for i in range(m):
            for j in range(n):
                g = rooms[i][j]
                if g == 0:
                    q = [(i,j)]; visited={}
                    while q:
                        rr = q.pop(0)
                        ii = rr[0]; jj = rr[1]
                        visited[rr]=1
                        stage = rooms[ii][jj] + 1
                        for nb in [(ii-1,jj),(ii+1,jj),(ii,jj-1),(ii,jj+1)]:
                            if (-1<nb[0]<m and -1<nb[1]<n and nb not in visited
                                and rooms[nb[0]][nb[1]]>0):
                                q.append(nb);visited[nb]=1
                                rooms[nb[0]][nb[1]] = min(stage,rooms[nb[0]][nb[1]])
        print('\n'.join([''.join(['{:4}'.format(item) for item in row])
      for row in rooms]))



rooms = [[0,100,-1,100,100,-1,-1,0,0,-1,100,100,0,-1,100,100,100,100,0,100,0,-1,-1,-1,-1,100,-1,-1,100,100,-1,-1,0,0,-1,0,0,0,100,0,100,-1,-1,0,-1,0,0,0,100],[100,0,-1,100,0,-1,-1,-1,-1,0,0,100,100,-1,-1,100,-1,-1,100,100,-1,0,-1,100,0,100,-1,100,0,100,0,100,-1,100,0,100,-1,100,0,100,100,0,-1,100,-1,-1,-1,0,100]]
wallsAndGates(rooms)
