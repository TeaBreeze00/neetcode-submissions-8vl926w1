"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""
import copy
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        # This is the plan, we'll just run a BFS/DFS from one of the nodes, then we'll have to 
        # make sure the connection is made at the right points by keeping a map that maps from the points to other points
        if not node:
            return None

        def dfs(node: Node):
            stack = []
            oldToNew = defaultdict(Node)
            stack.append(node)
            oldToNew[node] = Node(node.val)

            while stack:
                n = stack.pop()
                for nei in n.neighbors:
                    if nei not in oldToNew:
                        oldToNew[nei] = Node(nei.val)
                        stack.append(nei) 
                    oldToNew[n].neighbors.append(oldToNew[nei]) 

            return oldToNew[node]        

        return dfs(node)     



        