# L743. Network Delay Time
# Dijkstra, use min heap to store (distance from source, node), always relax
# using the min distance (top of heap) node's outgoing edges
# Observe that dist[node] = p is stored using popped items, because for a given
# node, there could be updates to it along the line, only when its popped will
# it get the shortest distance.
dk = collections.defaultdict(list)
for u,v,w in times:
    dk[u].append((v,w))

pq = [(0,K)] # need to sort by time, so put time first
dist = {}
while pq:
    p, node = heapq.heappop(pq)
    # if node already relaxed in previous turns, no need to relax anymore
    if node in dist: continue
    dist[node] = p
    for nb, d in dk[node]:
        if nb in dist: continue
        heapq.heappush(pq, (d+p, nb))

# if not all nodes are visited, return -1
return max(dist.values()) if len(dist) == N else -1

# Bellman-Ford, for V number of nodes, relax all E edges V-1 times.
# basically brute force. Doesn't matter where to start first, doesn't have
# to start from source. Only use this when negative weights exists, otherwise
# slow.
dist = collections.defaultdict(int)
dist[K] = 0
for _ in range(N-1):
    for u,v,w in times:
        if u in dist and dist[u] + w < dist.get(v, float('inf')):
            dist[v] = dist[u] + w

return max(dist.values()) if len(dist) == N else -1
