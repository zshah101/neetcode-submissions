class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        cMap = {}
        for i in range(numCourses):
            cMap[i] = []
        
        for course, preq in prerequisites:
            cMap[course].append(preq)
        
        visited = set()
        cycle = set()

        res = []
            
        def dfs(course):
            if course in cycle:
                return True
            if course in visited:
                return False
            visited.add(course)

            for preq in cMap[course]:
                if not dfs(preq): return False
            visited.remove(course)
            cycle.add(course)
            res.append(course)
            return True

        for course in range(numCourses):
            if not dfs(course): return []
        return res