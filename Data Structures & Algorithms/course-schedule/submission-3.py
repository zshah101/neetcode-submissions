class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        cMap = {}
        for i in range(numCourses):
            cMap[i] = []
        for course, preq in prerequisites:
            cMap[course].append(preq)
        # { 0: [1], 1: [2], 2:[] }

        visited = set() #1, 2

        def dfs(course):
            if cMap[course] == []:
                return True
            if course in visited:
                return False
            
            visited.add(course)

            for preq in cMap[course]:
                if not dfs(preq): return False

            visited.remove(course)
            cMap[course] = []
            return True
  
        for course in range(numCourses):
            if not dfs(course): return False
        return True 

