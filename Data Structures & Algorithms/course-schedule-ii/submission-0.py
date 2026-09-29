class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        pre_map = {}
        for i in range(numCourses):
            pre_map[i] = []

        for course, preq in prerequisites:
            pre_map[course].append(preq)

        visited = set ()
        cycle = set ()

        res = []
        def dfs(course):
            if course in visited:
                return False
            if course in cycle:
                return True
            
            visited.add(course)

            for preq in pre_map[course]:
                if not dfs(preq): return False
            visited.remove(course)
            cycle.add(course)
            res.append(course)
            return True

        for course in range(numCourses):
            if not dfs(course): return []
        return res


        