"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        map = {} # original : clone 


        def dfs(node):
            if node is None: return None 
            if node in map: return map[node]

            clone = Node(node.val)
            map[node] = clone

            for n in node.neighbors:
                clone.neighbors.append(dfs(n))
            return clone
        
        return dfs(node)







        