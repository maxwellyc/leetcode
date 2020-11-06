import collections
import heapq
def minCostToSupplyWater(n, wells, pipes):
    # minimum spanning tree problem
    # create a well node as source, all villages are connected to it
    # we're trying to find a minimum spanning tree.
    # the tree is acyclic, otherwise we're wasting an edge
    # need to create weighted edge
    method = 'Kruskal' # 'Kruskal'

    if method == 'Prim':
    # Prim
    # If we use Prim's algorithm, we pick a minimum cost edge that is
    # connected to the current tree (meaning currently we have a tree,
    # so this new edge should have one and only one vertex in the
    # current set)
    # we also maintain a priority queue, everytime we add an edge, we
    # push all it's connecting edges into queue. next time we pop the min
    # from this queue, we check if it doesn't form cycle using the above method
    # start with min_e
        # preprocess
        edges = collections.defaultdict(set) # store u: {(cost, v),...}
        min_e = (float('inf'),[])
        for ind,w in enumerate(wells):
            # house number actually ind+1
            # wells is index 0
            edges[0].add((w,ind+1))
            edges[ind+1].add((w,0))
            if w < min_e[0]:
                min_e = (w, [0,ind+1])

        for u,v,cost in pipes:
            edges[u].add((cost,v))
            edges[v].add((cost,u))
            if cost < min_e[0]:
                min_e = (cost, [u,v])
        A = set(min_e[1])
        ans = min_e[0]
        pq = []
        for item in (edges[min_e[1][0]] | edges[min_e[1][1]]):
            heapq.heappush(pq, item)

        while len(A) < n+1:
            cost, new_v = heapq.heappop(pq)
            if new_v not in A:
                ans += cost
                A.add(new_v)
                for cost, new_u in edges[new_v]:
                    if new_u not in A:
                        heapq.heappush(pq, (cost,new_u))
        return ans

    elif method == 'Kruskal':
    # Kruskal
    # If we use Kruskal, we need to design DSU (disjoint set union)
    # to find to detect cycle since we could be forming a forest at early stage.
    # also use minheap to maintain
        edges = []
        for ind,w in enumerate(wells):
            # house number actually ind+1
            # wells is index 0
            edges.append((w,(0,ind+1)))
        heapq.heapify(edges)

        for u,v,cost in pipes:
            heapq.heappush(edges,(cost,(u,v)))

        parent = [i for i in range(n+1)]

        # Use Disjoint Set Union to detect cycles
        # path compression
        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]

        def union(x,y):
            parent_x, parent_y = find(x), find(y)
            if parent_x == parent_y:
                return False
            parent[parent_x] = parent_y
            return True

        count = 0
        ans = 0
        # we have V = n+1 vertices, end computation at E = V-1 = n
        while count < n:
            cost, (u, v) = heapq.heappop(edges)
            while not union(u,v):
                cost, (u, v) = heapq.heappop(edges)
            count += 1
            ans += cost
        return ans

n = 5
wells = [46012,72474,64965,751,33304]
pipes = [[2,1,6719],[3,2,75312],[5,3,44918]]

print (minCostToSupplyWater(n, wells, pipes))
