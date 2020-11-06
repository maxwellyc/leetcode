matrix = [
 [ 1, 2, 3 ],
 [ 4, 5, 6 ],
 [ 7, 8, 9 ]
]
direction = 1 # 1 for northeast, -1 for southwest
m = len(matrix)
n = len(matrix[0])
ans = []
def nextInd(i,j,direction):
    org = matrix[i][j]
    if  org == 3: print (i,j,direction)
    if i>=m or j>=n:
        return None, None
    if direction == 1:
        if i != 0:
            if j+1 <n:
                i -= 1
                j += 1
            else:
                direction = -1
                i += 1
        else:
            direction = -1
            if j+1<n:
                j += 1
            else:
                i += 1
    else:
        if i != m-1:
            if j != 0:
                i += 1
                j -= 1
            else:
                direction = 1
                i += 1
        else:
            direction = 1
            j += 1
    if org == 3:  print (i,j, direction)
    return (i,j),direction

ind,direction = (0,0),1
count = 0
while ind and count<15:
    i, j = ind[0],ind[1]
    print (matrix[i][j],"start")
    ans.append(matrix[i][j])
    ind,direction = nextInd(i,j,direction)
    print (matrix[ind[0]][ind[1]],"next")
    count+=1
