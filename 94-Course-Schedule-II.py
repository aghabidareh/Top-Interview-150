class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        indegree, adj = [0 for i in range(numCourses)], [[] for i in range(numCourses)]
        for i in prerequisites:
            adj[i[1]].append(i[0])
            indegree[i[0]] += 1

        queue = deque([])
        for i in range(numCourses):
            if indegree[i] == 0:
                queue.append(i)

        topo = []
        if not queue:
            return []
        while (queue):
            x = queue.popleft()
            topo.append(x)
            for i in adj[x]:
                indegree[i] -= 1
                if indegree[i] == 0:
                    queue.append(i)

        if len(topo) == numCourses:
            return topo
        return []