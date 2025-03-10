class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        pre = [set() for _ in range(numCourses)]
        for prereq, course in prerequisites:
            pre[course].add(prereq)

        def dfs(x, visited, course):
            if course in pre[x]:
                return False
            visited.add(x)
            for i in pre[x]:
                if i not in visited:
                    if not dfs(i, visited, course):
                        return False
            return True

        for course in range(numCourses):
            if not dfs(course, set(), course):
                return False
        return True