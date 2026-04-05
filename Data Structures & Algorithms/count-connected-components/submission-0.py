class DSU:
    def __init__(self, n):
        # just a list of parents of each node in the list
        self.parent = list(range(n))

    def find(self, node):
        curr = node
        while curr != self.parent[curr]:
            curr = self.parent[curr]
        return curr    


    def union(self, u, v):
        pu = self.find(u)
        pv = self.find(v)
        if pu == pv:
            return False
        self.parent[pv] = pu
        return True

class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        dsu = DSU(n)
        res = n
        for u, v in edges:
            if dsu.union(u, v):
                res -= 1
        return res        