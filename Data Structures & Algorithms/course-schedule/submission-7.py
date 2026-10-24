class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = defaultdict(list)
        for a, b in prerequisites:
            graph[a].append(b)
        
        taken = set()
        taking = set()


        def dfs(course):
            if course in taken: return True
            if course in taking: return False

            taking.add(course)
            for pre in graph[course]:
                if not dfs(pre):
                    return False
            
            taking.remove(course)
            taken.add(course)
            return True
        

        for c in range(numCourses):
            if not dfs(c):
                return False
        return True


        