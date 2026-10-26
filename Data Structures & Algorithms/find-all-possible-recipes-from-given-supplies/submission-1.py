from collections import defaultdict, deque

class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        graph = defaultdict(list) # ingredient : [r]
        missing = {} # recipes : num_missing
        res = []
        queue = deque(supplies)
        seen = set(supplies)

        for r, ingredient in zip(recipes,ingredients):
            missing[r] = len(ingredient)
            for i in ingredient:
                graph[i].append(r)
        
        while queue:
            item = queue.popleft()
            for r in graph[item]:
                missing[r] -= 1
                if missing[r] == 0:
                    res.append(r)
                    if r not in seen:
                        seen.add(r)
                        queue.append(r)
        
        return res

