
matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]
m = len(matrix)
#if not m: return []
n = len(matrix[0])
# right, bottom, left, top (so we can cycle which wall to check)
walls = [n,m,-1,-1]
ind = [0,0]
ans = []
# can use complex number as direction, due to rotation properties
# but then that requires changing matrix into dictionary, which we won't do
# since there's extra work. we can simply store direction (increments) in a box
directions = [(0,1),(1,0),(0,-1),(-1,0)]
d = 0 # index for directions and walls

while len(ans) < m*n :
    ans.append(matrix[ ind[0] ][ ind[1] ])
    print (d, ind, walls)
    # determine which way we're going, if going :
    # right: d=0; down: d=1; left: d=2; up: d=3
    # check corresponding walls, worry about concise of code later
    if ind[(d+1)%2]+1 == walls[d] or ind[(d+1)%2]-1 == walls[d]:
        walls[d-1] = ind[d%2]
        d = (d+1)%4
    #ind = [i+directions[d][order%2] for order,i in enumerate(ind)]
    ind[0] += directions[d][0]
    ind[1] += directions[d][1]
    print (ind)

print (ans)
