class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        pref_map = {}
        for i in range(numCourses):
            pref_map[i] = []
        for course, preq in prerequisites:
            pref_map[course].append(preq)
        
        visited = set()

        def dfs(course):
            if course in visited:
                return False
            if pref_map[course] == []:
                return True
            visited.add(course)
            for preq in pref_map[course]:
                if not dfs(preq): return False
            visited.remove(course)
            pref_map[course] = []
            return True 
        for course in range(numCourses):
            if not dfs(course): return False
        return True