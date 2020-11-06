# Union Find
# default parent to 0, if 0, means that index is itself a parent
parent = list(range(len(vertices)))
def find(x):
  if parent[x] != x:
     parent[x] = find(parent[x])
  # this will reset the parent when needed.
  return parent[x]

def union(x, y):
  rootX, rootY = find(x), find(y)
  if rootX == rootY:
    return False
  # no union by rank, just random union.
  parent[rootX] = rootY
  return True


# (Basic) Disjoint Set Union without Union by Rank
class DSU:
    def __init__(self):
        self.par = range(1001)
    def find(self, x):
        if self.par[x] != x:
            self.par[x] = self.find(self.par[x])
        return self.par[x]
    def union(self, x, y):
        self.par[self.find(x)] = self.find(y)


#################################################
# Disjoint Set Union with Union by Rank
class DSU(object):
    def __init__(self):
        self.par = range(1001)
        self.rnk = [0] * 1001

    def find(self, x):
        if self.par[x] != x:
            self.par[x] = self.find(self.par[x])
        return self.par[x]

    def union(self, x, y):
        xr, yr = self.find(x), self.find(y)
        if xr == yr:
            return False
        elif self.rnk[xr] < self.rnk[yr]:
            self.par[xr] = yr
        elif self.rnk[xr] > self.rnk[yr]:
            self.par[yr] = xr
        else:
            self.par[yr] = xr
            self.rnk[xr] += 1
        return True

class Solution(object):
    def findRedundantConnection(self, edges):
        dsu = DSU()
        for edge in edges:
            if not dsu.union(*edge):
                return edge
