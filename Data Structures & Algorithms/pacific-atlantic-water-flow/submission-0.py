from collections import deque
class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        # Here's the dealio, I'm going to see what cells the cells adjacent to pacific water
        # flow goes to, then I'm going to see what cells the cells adjacent to atlantic water 
        # goes to, then the intersection of these two type of cells will give us the cells from where
        # waters from both oceans pass
        rows, cols = len(heights), len(heights[0])
        p_visit = set()
        p_queue = deque()
        a_visit = set()
        a_queue = deque()
        direction = [(-1,0), (1,0), (0,-1), (0,1)]
        
        # Now you should onboard the rows and columns adjacent to pacific and atlantic ocean to the queque and visited set
        for r in range(rows):
            p_visit.add((r, 0))
            p_queue.append((r, 0))
            a_visit.add((r, cols-1))
            a_queue.append((r, cols-1))

        for c in range(cols):
            p_visit.add((0, c))
            p_queue.append((0, c))
            a_visit.add((rows-1, c))
            a_queue.append((rows-1, c))

        def bfs(queue, visit):
            while queue:
                m, n = queue.popleft()
                for i, j in direction:
                    a, b = m + i, n + j
                    if (a,b) not in visit and 0 <= a < rows and 0 <= b < cols and heights[a][b] >= heights[m][n]:
                        visit.add((a,b))
                        queue.append((a,b))

        bfs(p_queue, p_visit)
        bfs(a_queue, a_visit)
        
        return list(p_visit.intersection(a_visit))
        










        


        

        