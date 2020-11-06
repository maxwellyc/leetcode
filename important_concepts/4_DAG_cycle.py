# Can also check if topological sort (using indegrees) ordering equals to
# number of vertices. Remember to initialize stack with isolated vertices too.

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # DAG find cycle, if cycle, return false
        # white is unvisited, black is totally visited, gray is visiting
        white, black = set(range(numCourses)), set()
        edges = collections.defaultdict(list)
        # v points to u, u need v to unlock.
        for u, v in prerequisites:
            edges[u].append(v)

        if len(edges) >= numCourses: return False

        def dfs(u, gray):
            for v in edges.get(u, []):
                if v in gray:
                    return False
                elif v not in black:
                    if not dfs(v, gray+{v}): return False
            black.add(u)
            return True

        for u in edges:
            if not dfs(u, set()): return False
        return True

# incoming edge degree method
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # start from courses with no prereq and do dfs
        # course has no prereq if no incoming edges
        incoming = [0]*numCourses
        edges = collections.defaultdict(list)
        order = []
        for i, j in prerequisites:
            incoming[i] += 1
            edges[j].append(i)


        queue = collections.deque([i for i in range(numCourses) if incoming[i] == 0])
        while queue:
            cur = queue.popleft()
            order.append(cur)
            for i in edges[cur]:
                incoming[i] -= 1
                if incoming[i] == 0:
                    queue.append(i)
        return order if len(order) == numCourses else []
