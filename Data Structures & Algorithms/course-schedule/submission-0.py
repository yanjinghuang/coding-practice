from collections import defaultdict
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = defaultdict(list)
        for a, b in prerequisites:
            graph[a].append(b)

        
        visited = set()
        visiting = set()

        def dfs(course):
            if course in visited: return True 
            if course in visiting: return False 

            visiting.add(course)
            for pre in graph[course]:
                if not dfs(pre):
                    return False
            visiting.remove(course)
            visited.add(course)
            return True

        for c in range(numCourses):
            if not dfs(c):
                return False
        return True
       