from collections import defaultdict, deque
class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        # {ingredent:[recipt]}
        graph = defaultdict(list)
        # {recipes: missing#}
        missing = {}
        # queue
        queue = deque(supplies)
        # hashset
        seen = set(supplies)
        res = []

        for r, ings in zip(recipes, ingredients):
            missing[r] = len(ings)
            for i in ings:
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

       



